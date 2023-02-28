from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            age = form.cleaned_data.get('age')
            gender = form.cleaned_data.get('gender')
            marital_status = form.cleaned_data.get('marital_status')
            mobile = form.cleaned_data.get('mobile')
            user = User.objects.get(username=username)
            user_data = Profile.objects.create(user=user, age=age, gender=gender, marital_status=marital_status, mobile=mobile)
            user_data.save()
            messages.success(request, f"Your account has been created ! You are now able to log in")
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

