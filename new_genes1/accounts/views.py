from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from Gene.urls import *
# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email']
            )
            auth.login(request, user)
            return redirect('home')
        return render(request, 'accounts/signup.html', {'error' : '비밀번호를 일치하게 해주세요!\n이메일 형식을 확인 해 주세요!!'})
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'accounts/login.html', {'error' : '아이디 또는 패스워드가 일치하지 않습니다!!'})
    return render(request, 'accounts/login.html')