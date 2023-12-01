from django.urls import path
from apps.general.views import AboutView, ContactView


app_name = "general"


urlpatterns = [
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
]
