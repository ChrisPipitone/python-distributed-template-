from fastapi import APIRouter

from backend.app.core.celery_app import celery_app

router = APIRouter()


@router.post("/trigger")
async def trigger_task(data: dict):
    """
    Example endpoint to trigger a background task.
    """
    task = celery_app.send_task("worker.app.tasks.sample_task", args=[data])
    return {"task_id": task.id, "status": "triggered"}
