from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpadateForm,ProfileUpadteForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form =  UserRegisterForm()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return  redirect('login')
    else:
        form =  UserRegisterForm()
    return render(request,'users/register.html', {'form' : form})

@login_required
def profile(request):
    u_form = UserUpadateForm(instance=request.user)
    p_form = ProfileUpadteForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html')
    