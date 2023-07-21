from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

class Note(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    last_updated = models.DateTimeField(auto_now=True)
    bg_color = models.CharField(max_length=50, default='#FFFFFF')
    category = models.ForeignKey(Category, null=True , on_delete=models.PROTECT)


