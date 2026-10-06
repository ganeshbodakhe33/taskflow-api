from fastapi import APIRouter, HTTPException

from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_service import create_task, get_task


router = APIRouter()


@router.post("/", response_model=TaskResponse)
def create_new_task(task: TaskCreate):
    return create_task(task)


@router.get("/{task_id}", response_model=TaskResponse)
def get_existing_task(task_id: int):
    task = get_task(task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task