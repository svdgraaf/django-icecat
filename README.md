django-icecat
=============

Django Icecat integration

Installation
============
Install the package, and add it to your applications:

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
ICECAT_API_LANGUAGE = 1  # The language you want to import, defaults to 1 (EN), NL = 2, See LanguageList.xml for other languages
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
If you want to import all the products, it is advised to first import the categories and suppliers

TODO
====
Lots :)

Requirements
============
South, lxml, ElementTree