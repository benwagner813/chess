from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def login(request):
    return render(request, 'account/login.html', {})

def register(request):
    return render(request, 'account/register.html', {})

def registerRequest(request):
    username = request.POST['username']
    password = request.POST['password']
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    user.first_name = firstName
    user.last_name = lastName
    user.save()
    return HttpResponseRedirect('/account/login')
