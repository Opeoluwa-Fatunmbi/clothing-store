from django.db import models
from apps.common.models import BaseModel
from django.db.models import Q

# Create your models here.


class SiteDetail(BaseModel):
    name = models.CharField(max_length=200, default="Clothing store")
    email = models.EmailField(default="email@gmail.com")
    desc = models.TextField(null=True)
    fb = models.URLField(verbose_name="Facebook", default="https://www.facebook.com/")
    tw = models.URLField(verbose_name="Twitter", default="https://twitter.com/")
    ig = models.URLField(verbose_name="Instagram", default="https://www.instagram.com/")
    ln = models.URLField(verbose_name="LinkedIn", default="https://www.linkedin.com/")
    working_hours = models.CharField(max_length=200, default="Mon - Fri: 8AM - 10PM")

    class Meta:
        verbose_name = "Site Detail"
        verbose_name_plural = "Site Details"
        # constraints = [
        #    # Ensures that only one instance of this model exists
        #    models.CheckConstraint(
        #        check=~Q(id__isnull=False), name="unique_site_detail_id"
        #    ),
        # ]

    def __str__(self):
        return self.name


ROLE_CHOICES = (
    ("Co-Founder", "Co-Founder"),
    ("Product Expert", "Product Expert"),
    ("Chief Marketing", "Chief Marketing"),
    ("Product Specialist", "Product Specialist"),
    ("Product Photographer", "Product Photographer"),
    ("General Manager", "General Manager"),
)


class TeamMember(BaseModel):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, choices=ROLE_CHOICES)
    desc = models.TextField(null=True)
    avatar = models.ImageField(upload_to="team/", null=True)
    fb = models.URLField(verbose_name="Facebook", default="https://www.facebook.com/")
    tw = models.URLField(verbose_name="Twitter", default="https://twitter.com/")
    ig = models.URLField(verbose_name="Instagram", default="https://www.instagram.com/")
    ln = models.URLField(verbose_name="LinkedIn", default="https://www.linkedin.com/")

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.name


class Message(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.name
