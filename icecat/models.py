from django.db import models


class Product(models.Model):
    model_name = models.CharField(max_length=255)
    part = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thumbnail = models.URLField(max_length=1024, default='')
    supplier = models.ForeignKey('Supplier')
    category = models.ForeignKey('Category')


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    logo = models.URLField(max_length=1024, default='')


class Category(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.URLField(max_length=1024, default='')
    description = models.TextField(default='')
    keywords = models.TextField(default='')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
