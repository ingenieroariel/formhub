DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'STORAGE_ENGINE': 'MyISAM',
        'NAME': 'formhub_dev',
        'USER': 'root',        # Not used with sqlite3.
        'PASSWORD': '',        # Not used with sqlite3.
        'HOST': 'localhost',
        'PORT': '',            # Set to empty string for default. Not used with sqlite3.
    },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'formhub_test.sqlite3',  # Or path to database file if using sqlite3.
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

