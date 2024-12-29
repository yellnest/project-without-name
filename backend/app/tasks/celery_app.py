from celery import Celery
from celery.schedules import crontab

from app.config import settings

celery_app = Celery(
    'tasks',
    broker=settings.get_redis_url(),
    include=['app.tasks.tasks'],
    broker_connection_retry_on_startup=True,
)

# celery_app.conf.beat_schedule = {
#     'clear_sessions': {
#         'task': 'app.tasks.clear_sessions',
#         # 'schedule': crontab(hour="0", minute="0", day_of_week="0"),
#         'schedule': crontab(minute='*/1'),
#     }
# }
#
# celery_app.conf.timezone = 'UTC'
