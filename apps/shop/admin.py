from django.contrib import admin
from .models import Category, Product, Review

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at", "updated_at")
    list_filter = list_display


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "in_stock", "created_at", "updated_at")
    list_filter = list_display


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "rating", "created_at", "updated_at")
    list_filter = list_display


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
