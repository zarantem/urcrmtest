from sqlmodel import SQLModel, Field, Relationship
from enum import Enum as PyEnum
from datetime import datetime
from typing import Optional


class TaskStatus(str, PyEnum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    REVIEW = "REVIEW"
    TESTING = "TESTING"
    DONE = "DONE"


class TaskModel(SQLModel, table=True):
    __tablename__ = "tasks"

    id: int = Field(primary_key=True)
    title: str = Field(nullable=False)
    description: Optional[str] = Field(default=None)
    status: TaskStatus = Field(default=TaskStatus.TODO)
    estimate: Optional[float] = Field(default=None)  # Оценка времени в часах
    deadline: Optional[datetime] = Field(default=None)  # Дедлайн задачи
    team: Optional[str] = Field(default=None)  # Название команды
    priority: int = Field(default=5, nullable=False)  # Приоритет задачи от 1 до 10
    tags: Optional[str] = Field(default=None)  # Теги, разделенные запятой
    executor_id: Optional[int] = Field(default=None, foreign_key="users.id")
    project_id: int = Field(foreign_key="projects.id")
    
    executor: Optional["Users"] = Relationship(back_populates="tasks")
    project: Optional["Projects"] = Relationship(back_populates="tasks")