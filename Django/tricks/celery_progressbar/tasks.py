from celery import shared_task

from time import sleep

# celery -A celery_progressbar worker -l info

@shared_task(bind=True)
def go_to_sleep(self, duration):
    sleep(duration)
    return 'Done'