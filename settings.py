import os
import socket
ROOT_PROJECT_FOLDER = os.path.dirname( __file__)
FILL_PATH = lambda x: os.path.join( ROOT_PROJECT_FOLDER, x )
STATIC_PATH, TEMPLATE_PATH = map( FILL_PATH, ['static','templates' ] )
# Django settings for data project.

#if its production server, turn off debug
if socket.gethostname() == '2155529.pubip.peer1.net':
    DEBUG = False
else:
    DEBUG = True
#setting template debug to the same as debug
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Tyler Lane', 'tlane@news-leader.com'),
    #('Tyler Lane', 'tyler@nolongervalid.com'),
    ('Tyler Laen', 'tlane2@gannett.com'),
)

if socket.gethostname() == '2155529.pubip.peer1.net':
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
  EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
MANAGERS = ADMINS
if socket.gethostname() == '2155529.pubip.peer1.net':
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'dataleader',                      # Or path to database file if using sqlite3.
            'USER': 'dataleader',                      # Not used with sqlite3.
            'PASSWORD': 'd4t4leader',                  # Not used with sqlite3.
            'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'dataleader',                      # Or path to database file if using sqlite3.
            'USER': 'dataleader',                      # Not used with sqlite3.
            'PASSWORD': 'd4t4leader',                  # Not used with sqlite3.
            'HOST': '10.37.74.210',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
if DEBUG:
    MEDIA_ROOT = STATIC_PATH
else:
    MEDIA_ROOT = "/opt/django/data.news-leader.com/dataleader/static/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
if DEBUG:
    MEDIA_URL = '/static'
else:
    MEDIA_URL = 'http://data-media.news-leader.com'


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
if DEBUG:
    ADMIN_MEDIA_PREFIX = '/media/'
else:
    ADMIN_MEDIA_PREFIX = 'http://data-media.news-leader.com/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%1h5k(=s7#q1fu1b=%hz9f4@a3%u+mydz*e&p^8c&7sx50)il*'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    #cache
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'mobileesp.mobile.MobileDetectionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)


ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        'TIMEOUT': 60,
        'OPTIONS': {'MAX_ENTRIES': 10000}
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.databrowse',
    'django.contrib.humanize',
    'django.contrib.webdesign',
    'django.contrib.gis',
    'south',
    'calls',
    'zones',
    'warrants',
    'stories',
    #'beaches',
    'accounts',
    #'elections',
    #'ads',
    'feedback',
    'scheduler',
    'schools',
    'census',
    'restaurants',
    'trueozarks',
)
