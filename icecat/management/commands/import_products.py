from django.core.management.base import BaseCommand
from icecat.models import *
from icecat import settings
from datetime import datetime
import requests
from optparse import make_option


class Command(BaseCommand):
    help = 'Download products'
    args = '<index.xml>'

    def handle(self, *args, **options):
        # TODO: make this configurable?
        filename = args[0]

        with open(filename, "r") as f:
            # use cElement, it's faaaaaaaaast
            from cElementTree import iterparse
            context = iterparse(f, events=("start", "end"))

            # turn it into an iterator
            context = iter(context)

            # # get the root element
            event, root = context.next()

            # loop through suppliers
            for event, elem in context:
                if event == "end" and elem.tag == "file":
                    values = dict(elem.items())

                    supplier, created = Supplier.objects.get_or_create(pk=values['Supplier_id'])
                    category, created = Category.objects.get_or_create(pk=values['Catid'])

                    product = Product()
                    product.pk = values['Product_ID']
                    product.supplier = supplier
                    product.category = category
                    product.model_name = values['Model_Name']
                    product.part = values['Prod_ID']
                    product.created_at = datetime.strptime(values['Date_Added'], '%Y%m%d%H%M%S')
                    product.updated_at = datetime.strptime(values['Updated'], '%Y%m%d%H%M%S')
                    product.thumbnail = values['HighPic']
                    if values['On_Market'] == '1':
                        product.on_market = True
                    product.save()

                    print product.model_name, product.part
                    root.clear()
