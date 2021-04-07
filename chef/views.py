from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from .models import Post
import json
from .models import Post


def home(request):


    #context = {
        #'posts': Post.objects.all()
    #}
    posts = Post.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(posts, 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    
    
    return render(request, 'blog/home.html',{ 'posts':users} )

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'    # default template: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    # overide the form valid method
    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True

        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True

        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})