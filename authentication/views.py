from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm

# the login view
def login_page(request):
    login_form = LoginForm()
    message = ""
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            pasword = login_form.cleaned_data["password"]
            user = authenticate(
                username=username,
                pasword=pasword,
            )
            print("user : ", user, login_form.cleaned_data, username, pasword)
            if user is not None:
                login(request, user)
                message = f"bonjour {user.username} vous etes connecte"
                print("\n\n {request} \n\n")
            else:
                message = "Identifiant invalide !"

    return render(
        request,
        "authentication/login.html",
        context={"form": login_form, "message": message},
    )


# the logout function
def logout_user(request):
    logout(request=request)
    redirect("login")
