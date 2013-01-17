DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'emkaystudios_db',                      # Or path to database file if using sqlite3.
		'USER': 'emkaystudios_user',                      # Not used with sqlite3.
		'PASSWORD': 'emkaystudios_password',                  # Not used with sqlite3.
		'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
	}
}

# URL prefix for static files.
STATIC_URL = '/static/'

# Unique key for Django.
SECRET_KEY = '7t96wt*wb9c@szmmt=!a01z8#ic)fgx)mk+u0vaeht+5lj+_g0'

# Redis settings
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Set up Cache
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
		'LOCATION': '127.0.0.1:11211'
	}
}