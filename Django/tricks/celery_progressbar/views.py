from django.shortcuts import render
from time import sleep

from .tasks import go_to_sleep

def index(request):
    task = go_to_sleep.delay(5)

    return render(request, 'celery_progressbar/index.html', {'task_id': task.task_id})