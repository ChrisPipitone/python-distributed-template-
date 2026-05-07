from celery import Celery

from shared.core.config import settings

celery_app = Celery(
    "worker",
    broker=settings.celery_broker_url,
    include=["worker.app.tasks.sample_task"],
)

celery_app.conf.update(
    task_track_started=True,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
