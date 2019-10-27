# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse
from .forms import UserRegistrationForm
from .models import UserProfile
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from .forms import UserProfileForm,UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url=reverse_lazy('accounts:login'))
def profile(request):
    user_id = request.user.id
    return redirect('accounts:user_profile_update',pk=user_id)

def signup(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'registration/signup.html', {'form':form})
    else:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/signup.html', {'form':form})

@login_required(login_url=reverse_lazy('accounts:login'))
def UserProfileUpdate(request,pk):
    if request.method=='GET':
        user = User.objects.get(pk=pk)
        if user!=request.user:
            return redirect('accounts:user_profile_update',pk=request.user.id)
        else:
            try:
                profile_instance = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                form1 = UserProfileForm()
                val = 'Create'
            else:
                form1 = UserProfileForm(instance=profile_instance)
                val = 'Update'

            form2 = UserUpdateForm(instance=request.user)
            return render(request, 'accounts/user_profile_update.html',
                          {'form': form1, 'form2': form2, 'btn_label': val})

    if request.method=='POST':
        if 'form' in request.POST:
            try:
                profile_instance = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                form = UserProfileForm(request.POST)
                form.instance.user_id = request.user.id
                form.save()
            else:
                form = UserProfileForm(request.POST, instance=profile_instance)
                form.save()
            return redirect('accounts:user_profile_update',pk=request.user.id)

        if 'form2' in request.POST:
            form = UserUpdateForm(request.POST,instance=request.user)
            form.save()
            return redirect('accounts:user_profile_update', pk=request.user.id)



def success_page(request):
    if request.method=='GET':
        return HttpResponse('Successpage')


