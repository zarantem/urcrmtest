from sqlmodel import SQLModel, BigInteger

class ProjectBase(SQLModel):
    id: int
    
class ProjectResponse(ProjectBase):
    title: str | None
    chat_id: int | None
    chat_photo: str | None
    participant_id: int | None
    participant: str | None
    users: str | None
    
class ProjectCreate(ProjectResponse):
    pass

class ProjectUpdateFull(ProjectResponse):
    pass

class ProjectPartialUpdate(ProjectBase):
    title: str | None
    chat_id: int | None
    chat_photo: str | None
    participant_id: int | None
    participant: str | None
    users: str | None