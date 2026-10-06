from typing import Literal

from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    assignee_id: int | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    assignee_id: int | None = None
    status: Literal[
        "todo",
        "in_progress",
        "done",
    ]