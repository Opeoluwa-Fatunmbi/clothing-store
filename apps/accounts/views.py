from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
import sweetify
from django.contrib import messages

# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {"form": form}
        return render(request, "accounts/register.html", context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
        context = {"form": form}
        return render(request, "accounts/register.html", context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if not user:
                messages.error(request, "Invalid credentials")
                redirect("accounts:login")
            login(request, user)
            redirect("/")
        context = {"form": form}
        return render(request, "accounts/login.html", context)
