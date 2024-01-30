from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    # EMAIL VERIFICATION
    path(
        "verify-email/<uidb64>/<token>/<user_id>/",
        views.VerifyEmail.as_view(),
        name="verify-email",
    ),
    path(
        "resend-verification-email/",
        views.ResendVerificationEmail.as_view(),
        name="resend-verification-email",
    ),
    # PASSWORD RESET
    path(
        "reset-password/",
        views.CustomPasswordResetView.as_view(
            template_name="accounts/password-reset.html",
            html_email_template_name="accounts/password-reset-html-email.html",
        ),
        name="reset_password",
    ),
    path(
        "reset-password-sent/",
        views.CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.CustomPasswordResetConfirmView.as_view(
            template_name="accounts/password-reset-form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset-password-complete/",
        views.CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
