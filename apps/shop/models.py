from django.db import models
from apps.common.models import BaseModel
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _
from apps.accounts.models import User

# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=500)
    desc = models.TextField(_("description"), max_length=500)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    in_stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products/", null=True, blank=True)

    def __str__(self):
        return self.name
    

RATING_CHOICES = (
    (5, 5),
    (4, 4),
    (3, 3),
    (2, 2),
    (1, 1),
)

class Review(BaseModel):   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(choices=RATING_CHOICES)
    text = models.TextField()

    def __str__(self):
        return self.user.full_name
    



