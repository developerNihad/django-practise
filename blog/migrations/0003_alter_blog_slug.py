# Generated by Django 5.2 on 2025-04-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blog_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
