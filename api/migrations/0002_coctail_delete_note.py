# Generated by Django 4.2.2 on 2023-06-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coctail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(blank=True, max_length=200, null=True)),
                (
                    "image",
                    models.ImageField(
                        default="aperol_spritz-b0f28440.png", null=True, upload_to=""
                    ),
                ),
                ("description", models.TextField(null=True)),
            ],
        ),
        migrations.DeleteModel(name="Note",),
    ]
