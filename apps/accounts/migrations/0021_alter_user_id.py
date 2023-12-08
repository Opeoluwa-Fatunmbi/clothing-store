# Generated by Django 4.2.6 on 2023-12-08 19:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0020_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("a2b6747b-f3aa-41c2-af93-37e62de05027"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
