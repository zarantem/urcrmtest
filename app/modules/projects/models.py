from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class ProjectModel(SQLModel, table=True):
    __tablename__ = "projects"

    id: int = Field(primary_key=True)
    title: Optional[str] = Field(default=None)
    chat_id: Optional[int] = Field(default=None)
    chat_photo: Optional[str] = Field(default=None)
    participant_id: int = Field(foreign_key="users.id")  
    participant: Optional["Users"] = Relationship(back_populates="owned_projects")
    users: List["Users"] = Relationship(back_populates="projects", sa_relationship_kwargs={"secondary": "project_users"})