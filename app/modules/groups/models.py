from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class GroupModel(SQLModel, table=True):
    __tablename__ = "groups"

    id: int = Field(primary_key=True)
    group_query_id: Optional[int] = Field(default=None)
    group_title: Optional[str] = Field(default=None)
    user_id: int = Field(foreign_key="users.id")
    
    user: Optional["Users"] = Relationship(back_populates="groups")