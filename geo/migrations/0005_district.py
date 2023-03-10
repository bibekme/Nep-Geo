# Generated by Django 4.1.5 on 2023-01-18 13:27

from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("geo", "0004_province_is_obselete"),
    ]

    operations = [
        migrations.CreateModel(
            name="District",
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
                (
                    "idx",
                    shortuuidfield.fields.ShortUUIDField(
                        blank=True, editable=False, max_length=22
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                ("is_obselete", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=500)),
                (
                    "province",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="districts",
                        to="geo.province",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
                "abstract": False,
            },
        ),
    ]
