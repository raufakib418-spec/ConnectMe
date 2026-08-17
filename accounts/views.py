from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm


def home(request):
    return render(request, "accounts/home.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                f"Welcome to ConnectMe, {user.username}!"
            )

            return redirect("home")
    else:
        form = UserRegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("home")


@login_required
def profile(request):
    return render(
        request,
        "accounts/profile.html"
    )
