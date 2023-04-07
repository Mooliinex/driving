from django.contrib.auth import authenticate as auth_login, authenticate
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from polls_driving.form import LoginForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls_driving index.")


def login(request):
    template = loader.get_template('registration/login.html')
    context = {'form': LoginForm}

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            password = request.POST.get('password')
            email = request.POST.get('email')
            user = authenticate(email=email, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect("/app/planning/")
            else:
                print("Error")

        context['form'] = form
    return render(request, template, context)
