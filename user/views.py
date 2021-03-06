from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# creating a register view
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save() # saves form data when it is valid
            username = form.cleaned_data.get("username")
            # adding a flash message
            messages.success(request, f"Your account has been created. You are now able to log in.")
            return redirect("login")

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

# creating a profile view
@login_required
def profile(request):
    if request.method == "POST":
        # pass the current user's info to the form
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        # save the data from both forms only when both inputs are valid
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your profile has been updated")
            # avoid the redirect alert from browser when one reloads the page
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, "users/profile.html", context)