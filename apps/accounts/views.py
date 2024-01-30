from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
import sweetify
from django.contrib import messages
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordResetDoneView,
)
from apps.accounts.mixins import LogoutRequiredMixin
from apps.accounts.models import User
from .senders import SendEmail, email_verification_generate_token
from .forms import (
    CustomPasswordResetForm,
    CustomSetPasswordForm,
    LoginForm,
    RegisterForm,
)

# Create your views here.


class RegisterView(LogoutRequiredMixin, View):
    def get(self, request):
        form = RegisterForm()
        context = {"form": form}
        return render(request, "accounts/register.html", context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            SendEmail.verification(request, user)
            request.session["verification_email"] = user.email
            return render(request, "accounts/email-verification-request.html")

        context = {"form": form}
        return render(request, "accounts/register.html", context)


class LoginView(LogoutRequiredMixin, View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if not user:
                messages.error(request, "Invalid Credentials")
                return redirect("accounts:login")
            if not user.is_email_verified:
                request.session["verification_email"] = email
                SendEmail.verification(request, user)
                return render(
                    request,
                    "accounts/email-verification-request.html",
                    {"detail": "request", "email": user.email},
                )
            login(request, user)
            return redirect("/")
        context = {"form": form}
        return render(request, "accounts/login.html", context)


class VerifyEmail(LogoutRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs["uidb64"]
        token = kwargs["token"]
        user_id = kwargs["user_id"]
        try:
            user_obj = User.objects.get(id=user_id)
        except User.DoesNotExist:
            messages.error(request, "You entered an invalid link")
            return redirect(reverse("login"))

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=uid)
        except Exception as e:
            user = None

        request.session[
            "verification_email"
        ] = (
            user_obj.email
        )  # Restoring email to session (incase request was made from a different client)
        if user:
            if user.id != user_obj.id:
                messages.error(request, "You entered an invalid link")
                return redirect(reverse("login"))

            if email_verification_generate_token.check_token(user, token):
                user.is_email_verified = True
                user.save()
                messages.success(request, "Verification successful!")
                request.session["verification_email"] = None
                SendEmail.welcome(request, user)
                return redirect(reverse("login"))

        return render(
            request,
            "accounts/email-verification-failed.html",
            {"email": user_obj.email},
        )


class ResendVerificationEmail(LogoutRequiredMixin, View):
    def get(self, request):
        email = request.session.get("verification_email")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Not allowed")
            return redirect(reverse("login"))

        if user.is_email_verified:
            messages.info(request, "Email address already verified!")
            request.session["verification_email"] = None
            return redirect(reverse("login"))

        SendEmail.verification(request, user)
        messages.success(request, "Email Sent")
        return render(
            request,
            "accounts/email-verification-request.html",
        )


class CustomPasswordResetView(LogoutRequiredMixin, PasswordResetView):
    # Taken from django.contrib.auth.views
    form_class = CustomPasswordResetForm


class CustomPasswordResetConfirmView(LogoutRequiredMixin, PasswordResetConfirmView):
    # Taken from django.contrib.auth.views
    form_class = CustomSetPasswordForm


class CustomPasswordResetDoneView(LogoutRequiredMixin, PasswordResetDoneView):
    # This is unnecessary as it can be done in the urls. Its just so that I can pass in Logout Required Mixin Easily
    # Taken from django.contrib.auth.views
    template_name = "accounts/password-reset-sent.html"


class CustomPasswordResetCompleteView(LogoutRequiredMixin, PasswordResetCompleteView):
    # This is unnecessary as it can be done in the urls. Its just so that I can pass in Logout Required Mixin Easily
    # Taken from django.contrib.auth.views
    template_name = "accounts/password-reset-done.html"
