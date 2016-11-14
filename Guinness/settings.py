import os
import sys
from os import path

# Does not work in mod wsgi so use the next one
#BUILDOUT_PATH = path.split(path.abspath(path.join(path.dirname(sys.argv[0]))))[0]

BUILDOUT_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

APP_NAME = 'Guinness Nigeria'
PROJECT_NAME = 'guinnessnigeria'


#  DEBUG = False
DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {

        # uncomment the next two lines and comment the rest to switch to sqlite3
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'Guinness',
         'USER': 'postgres',
         'PASSWORD': 'murphy',
         'HOST': 'localhost',
         'PORT': '5432',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Lagos'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BUILDOUT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BUILDOUT_PATH, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BUILDOUT_PATH, 'env/django/contrib/admin/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'z^uq$7x5jn%1nove38w+crkd9k8pq4=p8v*$h%h93-)b88uu@7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
)

ANONYMOUS_USER_ID = -1

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'guinnessnigeria.middleware.NoCacheMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'preferences.context_processors.preferences_cp',
)

ROOT_URLCONF = 'Guinness.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'Guinness.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BUILDOUT_PATH, 'templates'),
    os.path.join(BUILDOUT_PATH, 'env/django/contrib/admin/templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'south',
    'ckeditor',
    'photologue',
    'preferences',
    'unobase',
    'unobase.tagging',
    'guinnessnigeria',
    'guinnessnigeria.about',
    'guinnessnigeria.brands',
    'guinnessnigeria.careers',
    'guinnessnigeria.investors',
    'guinnessnigeria.news_and_media',
    'guinnessnigeria.gn_foundation',
    'unobase.poll',
    'unobase.age_gate',
    'django.contrib.admin',
)



# CK Editor Settings
CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'uploads')
CKEDITOR_STATIC_PREFIX = '/static/ckeditor/'

# Unobase Settings
DEFAULT_IMAGE_CATEGORY_CHOICES = ((0, '0'),)


# Unobase API Settings
API_REQUEST_TYPE_CHOICES = ((0, '0'),)

# Country legal ages

COUNTRY_LEGAL_AGES = {'Nigeria': 18}


ALLOWED_HOSTS = ['*']
