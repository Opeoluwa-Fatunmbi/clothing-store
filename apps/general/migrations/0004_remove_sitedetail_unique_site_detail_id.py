# Generated by Django 4.2.6 on 2023-12-01 20:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("general", "0003_sitedetail_email_sitedetail_unique_site_detail_id"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="sitedetail",
            name="unique_site_detail_id",
        ),
    ]
