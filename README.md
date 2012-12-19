django-icecat
=============
Django Icecat integration

Documentation
=============
Be sure to checkout the official [IceCat documentation](https://nl.icecat.biz/forum.cgi?post=3331) before you start with importing any of the data.

Installation
============
Install the package, and add it to your applications:

```bash
$ pip install django-icecat
```

```python
INSTALLED_APPS = (
    ...
    'icecat',
    ...
)
```

Add your login credentials in settings.py

```python
# Required:
ICECAT_API_USERNAME = 'xyz'
ICECAT_API_PASSWORD = 'foobar'

# Optional:
ICECAT_API_LANGUAGE = 1  # The language you want to import, defaults to 1 (EN), NL = 2, See [LanguageList.xml](https://data.icecat.biz/export/level4/refs/LanguageList.xml.gz) for other languages
ICECAT_TMP_PATH = '/tmp'  # The path where the xml files will be stored for faster access. 
```

Be sure to run the migrations:
```bash
$ ./application/manage.py migrate icecat
```

And you can run the commands:
```bash
$ ./application/manage.py import_categories
$ ./application/manage.py import_suppliers
$ ./application/manage.py import_products [path to index or daily delta]
```
If you want to import all the products, it is advised to first import the categories and suppliers. Also: be sure to save up on Starbucks coupons, as a total product import can take quite a while.

TODO
====
Lots :)

Requirements
============
South, lxml, ElementTree, Requests