import sys

# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5rqoulof49akq',
        'USER': 'mhxjdgyjytgyzv',
        'PASSWORD': '888c7be10e5ca7eb03c06ccac4b4e6e26ac3e2bdcca2369b9540c25519a285ee',
        'HOST': 'ec2-54-217-225-16.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
        'CONN_MAX_AGE': 900
    }
}
