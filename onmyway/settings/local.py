from .base import *

#configuracion de la base de datos Local MYSQL

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'onmyway',
            'USER': 'Informatorio',
            'PASSWORD': 'Distorsiondemente2435424354',
            'HOST': 'localhost',
            'PORT': '',
        }
    }