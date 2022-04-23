from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import login
from django.conf import settings

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            print(form)
            print("INvlaie fgorme.")
            print(form.errors)
            return render(request, 'registration/register.html', {'form':form})
        messages.error(request, "Registration Failed.")
    form = RegistrationForm()
    return render(request = request, template_name = "registration/register.html", context={"form": form})




# def registerRequest(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     firstName = request.POST['firstName']
#     lastName = request.POST['lastName']
#     email = request.POST['email']
#     user = User.objects.create_user(username, email, password)
#     user.first_name = firstName
#     user.last_name = lastName
#     user.save()
#     return HttpResponseRedirect('/account/login')
