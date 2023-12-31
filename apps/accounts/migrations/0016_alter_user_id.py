# Generated by Django 4.2.6 on 2023-12-08 19:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0015_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("c74b3db7-183c-4301-a364-693bb4acc35a"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
