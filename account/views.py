from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/account/home/')
            return response
        else:
            return render(request, 'account/login.html', {'error': 'username or password is error'})
    return render(request, 'account/login.html')


def home(request):
    return render(request, 'django_sb_admin/sb_admin_dashboard.html')


def logout(request):
    auth.logout(request)
    return render(request, 'account/login.html')
