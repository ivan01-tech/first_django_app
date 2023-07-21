from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            if user:
                messages.success(request, "Register successfuly !")
                login(request=request, user=user)
                return redirect("home")
            else:
                form = RegisterUserForm()
                return render(
                    request,
                    "authentication/register_user.html",
                    {"form": form, "message": "Something went wrong !"},
                )

    else:
        form = RegisterUserForm()

    return render(request, "authentication/register_user.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "You are now connected !")
                return redirect("home")
            else:
                # message = ""
                messages.success(request, "Wrong crudentials")
                return redirect("login")
        else:
            message = "Username or password is missing !"
            return render(request, "authentication/login.html", {"message": message})

    else:
        return render(request, "authentication/login.html", {})


def logout_user(request):
    logout(request)
    return redirect("authentication:login")
