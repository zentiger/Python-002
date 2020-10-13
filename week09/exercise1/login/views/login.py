from ..form import LoginForms
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    if request.method == "POST":
        login_form = LoginForms(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = auth.authenticate(username=cd['username'], password=cd['password'])
            if user:
                auth.login(request,user)
                return HttpResponse('登录成功')
            else:
                return HttpResponse('登录失败')
    
    if request.method == "GET":

        login_form = LoginForms()
        return render(request, 'login.html', {'form': login_form})