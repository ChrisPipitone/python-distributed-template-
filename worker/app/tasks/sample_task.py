import logging

from worker.app.main import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(name="worker.app.tasks.sample_task")
def sample_task(data: dict):
    logger.info(f"Processing task with data: {data}")
    return {"result": "success", "processed_data": data}
