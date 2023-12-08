from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class SiteDetail(BaseModel):
    name = models.CharField(max_length=200, default="Clothing Store")
    desc = models.TextField(null=True)
    email = models.EmailField(default="clothingstore@gmail.com")
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=500, null=True)
    working_hours = models.CharField(max_length=200, default="Mon - Fri: 8AM - 10PM")

    maps_url = models.URLField(
        default="https://www.google.com/maps?q=10+Broad+Street,+Lagos,+Nigeria&z=13&ie=UTF8&iwloc=&output=embed"
    )

    fb = models.URLField(verbose_name=_("Facebook"), default="https://www.facebook.com")
    ig = models.URLField(
        verbose_name=_("Instagram"), default="https://www.instagram.com/"
    )
    tw = models.URLField(verbose_name=_("Twitter"), default="https://www.twitter.com/")
    ln = models.URLField(
        verbose_name=_("Linkedin"), default="https://www.linkedin.com/"
    )

    def __str__(self):
        return self.name

    # class Meta:
    #     constraints = [
    #         # Check constraint to allow only one data in table
    #         models.CheckConstraint(check=Count(Q(id__isnull=False), name="unique_site_detail"),
    #     ]


ROLE_CHOICES = (
    ("CO-Founder", "CO-Founder"),
    ("Product Expert", "Product Expert"),
    ("Chief Marketing", "Chief Marketing"),
    ("Product Specialist", "Product Specialist"),
    ("Product Photographer", "Product Photographer"),
    ("General Manager", "General Manager"),
)


class TeamMember(BaseModel):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, choices=ROLE_CHOICES)
    desc = models.CharField(max_length=300)
    avatar = models.ImageField(upload_to="team/")
    fb = models.URLField(verbose_name=_("Facebook"), default="https://www.facebook.com")
    ig = models.URLField(
        verbose_name=_("Instagram"), default="https://www.instagram.com/"
    )
    tw = models.URLField(verbose_name=_("Twitter"), default="https://www.twitter.com/")
    ln = models.URLField(
        verbose_name=_("Linkedin"), default="https://www.linkedin.com/"
    )

    def __str__(self):
        return self.name

    @property
    def avatar_url(self):
        try:
            url = self.avatar.url
        except:
            url = ""
        return url


class Message(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
