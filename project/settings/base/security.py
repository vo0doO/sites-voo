# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost',
                 'voo.asuscomm.com', 'kirsanov.ga', '192.168.1.4', 'sites-voo.herokuapp.com', '0.0.0.0']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

X_FRAME_OPTIONS = 'DENY'
