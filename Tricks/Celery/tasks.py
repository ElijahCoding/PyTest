from celery import Celery

# rbmq_broker = 'pyamqp://guest@localhost//'
app = Celery('tasks', broker='redis://localhost')

@app.task
def reverse(text):
    return text[::-1]

# celery -A tasks worker --loglevel=info
# celery worker --help