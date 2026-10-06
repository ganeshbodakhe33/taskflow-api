from fastapi import APIRouter, HTTPException

from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_service import create_task, get_task


router = APIRouter()


@router.post("/", response_model=TaskResponse)
def create_new_task(task: TaskCreate):
    return create_task(task)

@router.post("/health", response_model=TaskResponse)
def check_task_health():
    # This is a simple health check endpoint
    # In a real application, you might want to perform more comprehensive checks
    return TaskResponse(
        id=0,
        title="Health Check",
        description="Task for health check",
        assignee_id=None,
        status="todo"
    )
@router.post("/run", response_model=TaskResponse)
def run_task():
    # This is a simple endpoint to run a task
    # In a real application, you might want to implement the actual task execution logic
    return TaskResponse(
        id=0,
        title="Run Task",
        description="Task for running",
        assignee_id=None,
        status="todo"
    )

@router.get("/{task_id}", response_model=TaskResponse)
def get_existing_task(task_id: int):
    task = get_task(task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task
