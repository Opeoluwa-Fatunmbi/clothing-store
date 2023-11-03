from django.contrib import admin
from apps.accounts.models import *
from django.utils.translation import gettext_lazy as _

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "is_email_verified", "created_at"]
    list_filter = list_display

    fieldsets = (
        (
            _("Login Credentials"),
            {"fields": ("email","password")}
                
            ),
        ),
    )
    



admin.site.register(User, UserAdmin)