from .base import *


ADMINS = (
    ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{{cookiecutter.development_db_adapter}}',
        'NAME': '{{cookiecutter.development_db_schemaname}}',
        'USER': '{{cookiecutter.development_db_user}}',
        'PASSWORD': '{{cookiecutter.development_db_passwd}}',
        'HOST': '',
        'PORT': '',
    }
}



# You might want to use sqlite3 for testing in local as it's much faster.
if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.{{cookiecutter.development_db_adapter}}',
            'NAME': '{{cookiecutter.development_db_schemaname}}',
            'USER': '{{cookiecutter.development_db_user}}',
            'PASSWORD': '{{cookiecutter.development_db_passwd}}',
            'HOST': '',
            'PORT': '',
        }
    }
