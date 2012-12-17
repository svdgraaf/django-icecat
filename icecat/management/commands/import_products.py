from django.core.management.base import BaseCommand
from icecat.models import *
from icecat import settings
import requests
from optparse import make_option


class Command(BaseCommand):
    help = 'Download products'
    args = '<index.xml>'

    def handle(self, *args, **options):
        # TODO: make this configurable?
        filename = args[0]
        print filename

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
                if event == "end" and elem.tag == "Supplier":
                    values = dict(elem.items())

                    # get or update the supplier
                    supplier, created = Supplier.objects.get_or_create(name=values['Name'], pk=values['ID'])
                    if created:
                        print supplier.name + ' added'
                    root.clear()
                    