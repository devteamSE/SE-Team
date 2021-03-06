# Django settings for myproject project.

import sys
import os
import datetime

try:
	globals().update(vars(sys.modules['SETeam.settings']))
except:
	globals().update(vars(sys.modules['settings']))

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_PARENT = os.path.normpath(os.path.join(PROJECT_ROOT, '..'))
sys.path.insert(0, PROJECT_ROOT)

STATIC_ROOT			= os.path.join(PROJECT_PARENT, "static/")
MEDIA_ROOT 			= os.path.join(PROJECT_PARENT, "media/")

STATIC_URL			= '/static/'
MEDIA_URL 			= '/media/'
LOGIN_URL           = '/login/'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEVELOPMENT = DEBUG

EMAIL_HOST 			= 'smtp.webfaction.com'
EMAIL_HOST_USER 	= "seteam_info"
EMAIL_HOST_PASSWORD = "P@ssw0rd"
DEFAULT_FROM_EMAIL = 'info@seteam.willdev4food.com'
SERVER_EMAIL = 'info@seteam.willdev4food.com'

ADMINS = (
    ('Jeremy Welkley', 'jeremy@willdev4food.com'),
    ('Joshua Fisk', 'jcfisk@email.uark.edu',),
)

ADMIN_MEDIA_PREFIX = 'admin_media'

MANAGERS = ADMINS

# to use sqlite uncomment this section
# db_path = PROJECT_PARENT+'/SETeam/seteam_db.sqlite'
# DATABASES = {
# 	'default': {
# 	    'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
# 	    'NAME': db_path,                  # Or path to database file if using sqlite3.
# 	    # The following settings are not used with sqlite3:
# 	    'USER': '',
# 	    'PASSWORD': '',
# 	    'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
# 	    'PORT': '',                      # Set to empty string for default.
# 	}
# }

DATABASES = {
	'default': {
	    'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	    'NAME': 'seteam',                  # Or path to database file if using sqlite3.
	    # The following settings are not used with sqlite3:
	    'USER': 'joshua',
	    'PASSWORD': 'p@ssw0rd',
	    'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
	    'PORT': '5432',                      # Set to empty string for default.
	}
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['127.0.0.1:8000','seteam.willdev4food.com']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

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
# Example: "/var/www/example.com/media/"
# MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
# MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
# STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
# STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'lf##(g)cqcckh-40#6vzp+*0$3!4sr2y*g-3c$3#_8h!0#+jxq'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SETeam.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'SETeam.wsgi.application'

TEMPLATE_DIRS = (
	os.path.join(PROJECT_ROOT, "templates/"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
    'team',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.contrib.messages.context_processors.messages',
	"django.core.context_processors.request",
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'team.context_processors.user',
)