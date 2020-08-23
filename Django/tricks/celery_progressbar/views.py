from django.shortcuts import render
from time import sleep

from .tasks import go_to_sleep

def index(request):
    go_to_sleep.delay(5)
    return render(request, 'celery_progressbar/index.html')