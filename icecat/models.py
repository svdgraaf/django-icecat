from django.db import models
import requests
import hashlib
from icecat import settings


class Product(models.Model):
    model_name = models.CharField(max_length=255)
    part = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thumbnail = models.URLField(max_length=1024, default='')
    on_market = models.BooleanField(default=False)
    supplier = models.ForeignKey('Supplier')
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return u'{supplier} {name}'.format(supplier=self.supplier.name, name=self.name)

    def get_specifications(self):
        # check if the file is already present
        xml = self._get_raw_source()
        return xml

    def _get_raw_source(self):
        import os
        url = 'https://data.icecat.biz/xml_s3/xml_server3.cgi?prod_id={prod_id};vendor={vendor};lang={lang};output={output}'.format(prod_id=self.part, vendor=self.supplier.name, output='productxml', lang='EN')

        # check if filename is already downloaded
        filename = 'icecat-' + hashlib.md5(url).hexdigest() + '.xml'
        path = os.path.join(settings.TMP_PATH, filename)

        if not os.path.isfile(path):
            # File isn't present yet, let's download it
            r = requests.get(url, auth=(settings.API_USERNAME, settings.API_PASSWORD))
            f = open(path, 'wb')
            f.write(r.text)
            f.close()

            return r.text
        else:
            f = open(path, 'r')
            xml = f.read()
            f.close()
            return xml


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    logo = models.URLField(max_length=1024, default='')


class Category(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.URLField(max_length=1024, default='')
    description = models.TextField(default='')
    keywords = models.TextField(default='')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
