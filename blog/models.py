from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False,blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField()
    is_home = models.BooleanField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
