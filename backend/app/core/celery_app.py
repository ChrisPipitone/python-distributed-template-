from celery import Celery

from shared.core.config import settings

celery_app = Celery("worker", broker=settings.celery_broker_url)

celery_app.conf.task_routes = {
    "app.tasks.*": "main-queue",
}
