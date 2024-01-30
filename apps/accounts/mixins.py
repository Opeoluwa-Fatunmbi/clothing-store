from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.http import JsonResponse


class LogoutRequiredMixin(AccessMixin):
    """Verify that the current user is unauthenticated."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)


class LoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
                return JsonResponse(
                    {"status": "error", "message": "You must login first!"}
                )
            return redirect("/accounts/login/")
        return super().dispatch(request, *args, **kwargs)
