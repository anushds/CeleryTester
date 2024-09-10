from celery import Celery

app = Celery('tasks', broker='rabbitmq://localhost')

