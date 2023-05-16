from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['password1']
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken. Please choose a different username.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Sorry, this email is already registered. Please try another one.")
                return redirect('register')
            user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                            last_name=last_name, email=email)
            user.save()
            return redirect('login')

        else:
            messages.info(request,
                          "Oops! Passwords don't match. Please make sure both fields contain the same password.")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
