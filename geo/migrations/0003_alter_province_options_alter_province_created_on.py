# Generated by Django 4.1.5 on 2023-01-18 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geo", "0002_alter_province_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="province",
            options={"ordering": ["id"]},
        ),
        migrations.AlterField(
            model_name="province",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]