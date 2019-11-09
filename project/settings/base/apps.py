INSTALLED_APPS = (
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    
    'django_extensions',
    'clear_cache',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',

    'django_static_jquery',
    'multiselectfield',

    'django_robokassa',

    # your apps goes here
    # 'project.apps.myapp',

    'project.apps.curiosity',
    'project.apps.shop',
    'project.apps.bankrot',
    'project.apps.polls',
)
