from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'corey',
        'title' :'blog Post1',
        'content':'first post content',
        'date_posted' : 'august 27',
    },
    {
        'author':'corey',
        'title' :'blog Post2',
        'content':'first post content',
        'date_posted' : 'august 27',
    }
]
# Create your views here
def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html')
# Create your views here.
