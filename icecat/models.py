from django.db import models

class Product(models.Model):
    model_name = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    updated = models.DateTimeField()
    supplier = models.ForeignKey('Supplier')
    # Catid = 


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    logo = models.URLField(max_length=1024, default='')


class Category(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.URLField(max_length=1024, default='')
    description = models.TextField(default='')
    keywords = models.TextField(default='')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
