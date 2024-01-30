import threading
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
import six


class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.id)
            + six.text_type(timestamp)
            + six.text_type(user.is_email_verified)
        )


email_verification_generate_token = EmailVerificationTokenGenerator()


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class SendEmail:
    @staticmethod
    def verification(request, user):
        domain = f"{request.scheme}://{request.get_host()}"  # http
        subject = "Verify Your Email"
        context = {
            "domain": domain,
            "name": user.full_name,
            "uid": urlsafe_base64_encode(force_bytes(user.id)),
            "token": email_verification_generate_token.make_token(user),
            "user_id": user.id,
        }
        message = render_to_string("accounts/email-verification-message.html", context)
        email_message = EmailMessage(subject=subject, body=message, to=[user.email])
        email_message.content_subtype = "html"
        EmailThread(email_message).start()

    @staticmethod
    def welcome(request, user):
        domain = f"{request.scheme}://{request.get_host()}"  # http
        subject = "Account Verified"
        context = {
            "domain": domain,
            "name": user.full_name,
        }
        message = render_to_string("accounts/welcome-message.html", context)
        email_message = EmailMessage(subject=subject, body=message, to=[user.email])
        email_message.content_subtype = "html"
        EmailThread(email_message).start()
