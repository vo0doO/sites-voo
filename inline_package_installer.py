from ast import Continue
import subprocess

def install_packages():
    try:
        PACKAGES_LIST = "gunicorn, django, django_extensions, fabric, asgiref, async-timeout, attrs, autobahn, Automat, channels-redis, constantly, daphne, hiredis, hyperlink, idna, incremental, msgpack, PyHamcrest, pytz, six, Twisted, txaio, whitenoise, zope.interface, beautifulsoup4, bs4, certifi, chardet, dj-database-url, Pillow, python-dateutil, requests, soupsieve, sqlparse, urllib3, vk-api, django-multiselectfield, django-range-slider, django-phonenumber-field, phonenumbers, Importable, django-static-jquery, lxml, autopep8, defusedxml, django-allauth, django-countries, django-crispy-forms, oauthlib, pep8, pycodestyle, python-decouple, python3-openid, requests-oauthlib, stripe, watchdog, PyYAML, argh, reload, mypy, mypy-extensions, typing-extension"
        for package in PACKAGES_LIST.split(", "):   
            subprocess.getoutput(f"""python -m pip install {package}""")
            continue
    except Exception as e:
        print(e)
        Continue
        
install_packages()