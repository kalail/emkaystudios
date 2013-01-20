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
MEDIA_URL = '/media/'
# COMPRESS_URL = '/static/'

# Unique key for Django.
SECRET_KEY = '7t96wt*wb9c@szmmt=!a01z8#ic)fgx)mk+u0vaeht+5lj+_g0'

# Celery settings
BROKER_URL = 'amqp://guest:guest@localhost:5672//'

# Set up Cache
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
		'LOCATION': '127.0.0.1:11211'
	}
}

# Django debug toolbar
DEBUG_TOOLBAR_CONFIG = {
	'INTERCEPT_REDIRECTS': False,

}
INTERNAL_IPS = ('0.0.0.0',)
DEBUG_TOOLBAR_PANELS = (
	'debug_toolbar.panels.version.VersionDebugPanel',
	'debug_toolbar.panels.timer.TimerDebugPanel',
	'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
	'debug_toolbar.panels.headers.HeaderDebugPanel',
	'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
	'debug_toolbar.panels.template.TemplateDebugPanel',
	'debug_toolbar.panels.sql.SQLDebugPanel',
	'cache_panel.panel.CacheDebugPanel',
	'debug_toolbar.panels.signals.SignalDebugPanel',
	'debug_toolbar.panels.logger.LoggingPanel',
)