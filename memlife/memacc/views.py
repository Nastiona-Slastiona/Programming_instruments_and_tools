from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('date_of_birth')
    serializer_class = ProfileSerializer

@login_required
def dashboard(request):
    return render(request, 
                    'memacc/dashboard.html',
                    {'section': dashboard})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, 
                                    data=request.POST, 
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        if request.user is not None and hasattr(request.user,'profile'):
            profile_form = ProfileEditForm(instance=request.user.profile)
        else:
            Profile.objects.create(user=request.user)
            profile_form = ProfileEditForm()
        user_form = UserEditForm(instance=request.user)
    return render(request,
                    'memacc/edit.html',
                    {'user_form': user_form,
                    'profile_form': profile_form})

def google_reg(request):
    return render(request, 'socialaccount_connections')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'memacc/dashboard.html', {'form': form})
                else:
                    messages.error(request, 'Disabled account')
            else:
                messages.error(request, 'Invalid Username')
    else:
        form = LoginForm()
        return render(request, 'memacc/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'memacc/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'memacc/register.html', {'user_form': user_form})