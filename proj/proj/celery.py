import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
import django
django.setup()
app = Celery('proj')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_bday_wish': {
        'task': 'customers.tasks.send_bday_wish',
        'schedule': crontab(minute='*/1')
    },
    'update_bday_notified': {
        'task': 'customers.tasks.update_bday_wish',
        'schedule': crontab(minute='*/1')
    }
}