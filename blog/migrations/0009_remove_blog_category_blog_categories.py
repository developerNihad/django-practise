# Generated by Django 5.2 on 2025-04-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_blog_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="category",
        ),
        migrations.AddField(
            model_name="blog",
            name="categories",
            field=models.ManyToManyField(to="blog.category"),
        ),
    ]
