from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("products/", views.ProductsView.as_view(), name="products"),
]
