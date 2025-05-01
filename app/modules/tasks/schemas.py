from sqlmodel import SQLModel, BigInteger
from datetime import datetime

class TaskBase(SQLModel):
    id: int
    
class TaskResponse(TaskBase):
    title: str | None
    description: str | None
    status: str | None
    estimate: float | None
    deadline: datetime | None
    team: str | None
    priority: int | None
    tags: str | None
    executor_id: int | None
    project_id: int | None
    executor: str | None
    project: str | None
    
class TaskCreate(TaskResponse):
    pass

class TaskUpdateFull(TaskResponse):
    pass

class TaskPartialUpdate(TaskBase):
    title: str | None
    description: str | None
    status: str | None
    estimate: float | None
    deadline: datetime | None
    team: str | None
    priority: int | None
    tags: str | None
    executor_id: int | None
    project_id: int | None
    executor: str | None
    project: str | None