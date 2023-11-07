# Generated by Django 4.2.6 on 2023-11-07 22:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_alter_category_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
