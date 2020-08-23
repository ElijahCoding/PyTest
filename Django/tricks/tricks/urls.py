from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('celery_progressbar.urls')),
    path('celery_progresss', include('celery_progress.urls'))
]
