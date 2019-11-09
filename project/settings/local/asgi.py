import os


ASGI_APPLICATION = 'project.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": ["redis://h:p1cc1b2f3747536c5723c0ca24de09d3b13126df55e0fed3f0cfc7b87166a0baf@ec2-52-50-126-190.eu-west-1.compute.amazonaws.com:20909"],
            # "symmetric_encryption_keys": [SECRET_KEY],
            # local: '127.0.0.1'
            # AWS: 'REDIS-URL.amazonaws.com'
        },
    },
}
