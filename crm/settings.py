INSTALLED_APPS = [
    # existing apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crm',  # your app
    'django_crontab',  # <-- add this
]

# Cron job configuration
CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),
]