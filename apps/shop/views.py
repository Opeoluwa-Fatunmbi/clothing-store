from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from apps.shop.models import Category, Product


# Create your views here.
class HomeView(View):
    def get(self, request):
        products = Product.objects.all()[:6]
        categories = Category.objects.all()
        context = {
            "products": products,
            "categories": categories,
            "rating_range": range(5),
        }
        return render(request, "shop/home.html", context)


class ProductsView(ListView):
    model = Product
    paginate_by = 15
    template_name = "shop/products.html"
    context_object_name = "products"
