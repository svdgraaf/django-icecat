from django.core.management.base import BaseCommand
from icecat.models import *
from icecat import settings
import requests
import gzip


class Command(BaseCommand):
    help = 'Downloads latest suppliers list, and imports all suppliers'

    def handle(self, *args, **options):
        # download file
        r = requests.get('https://data.icecat.biz/export/level4/refs/SuppliersList.xml.gz', auth=(settings.API_USERNAME, settings.API_PASSWORD))

        tmp_filename = settings.TMP_PATH + '/suppliers.xml.gz'
        with open(tmp_filename, "wb") as f:
            f.write(r.content)

        # the suppliers list is gzipped
        f = gzip.open(tmp_filename, 'rb')

        # use cElement, it's faaaaaaaaast
        from cElementTree import iterparse
        context = iterparse(f, events=("start", "end"))

        # turn it into an iterator
        context = iter(context)

        # get the root element
        event, root = context.next()


        # loop through suppliers
        for event, elem in context:
            if event == "end" and elem.tag == "Supplier":
                values = dict(elem.items())

                # get or update the supplier
                supplier, created = Supplier.objects.get_or_create(name=values['Name'], pk=values['ID'])
                if created:
                    print supplier.name + ' added'
                root.clear()

        # close gzip file
        f.close()