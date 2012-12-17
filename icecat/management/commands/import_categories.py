from django.core.management.base import BaseCommand
from icecat.models import *
from icecat import settings
import requests
import gzip


class Command(BaseCommand):
    help = 'Downloads categories list, and imports all categories'

    def handle(self, *args, **options):
        # download file
        r = requests.get('https://data.icecat.biz/export/level4/refs/CategoriesList.xml.gz', auth=(settings.API_USERNAME, settings.API_PASSWORD))

        tmp_filename = settings.TMP_PATH + '/categories.xml.gz'
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
            if event == "end" and elem.tag == "Category":
                values = dict(elem.items())
                category, created = Category.objects.get_or_create(pk=values['ID'])

                # find description
                descriptions = elem.findall('Description')
                for descr in descriptions:
                    descr_values = dict(descr.items())
                    if descr_values['langid'] == str(settings.API_LANGUAGE):
                        category.description = descr_values['Value']

                # find name
                names = elem.findall('Name')
                for name in names:
                    name_values = dict(name.items())
                    if name_values['langid'] == str(settings.API_LANGUAGE):
                        category.name = name_values['Value']

                # see if we have a parent category
                parent = elem.find('ParentCategory')
                if parent:
                    parent = dict(parent.items())
                    category.parent_id = parent['ID']

                category.save()

                root.clear()

        # All done!