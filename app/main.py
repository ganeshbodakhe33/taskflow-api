from fastapi import FastAPI

from app.api.users import router as users_router
from app.api.tasks import router as tasks_router


app = FastAPI(
    title="TaskFlow API",
    version="1.0.0",
    description="REST API for managing users and tasks.",
)


app.include_router(
    users_router,
    prefix="/api/users",
    tags=["Users"],
)

app.include_router(
    tasks_router,
    prefix="/api/tasks",
    tags=["Tasks"],
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "taskflow-api",
    }