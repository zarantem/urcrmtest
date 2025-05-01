from sqlmodel import SQLModel, BigInteger

class GroupBase(SQLModel):
    id: int
    
class GroupResponse(GroupBase):
    group_query_id: int | None
    group_title: str | None
    user_id: int | None
    user: str | None
    
class GroupCreate(GroupResponse):
    pass

class GroupUpdateFull(GroupResponse):
    pass

class GroupPartialUpdate(GroupBase):
    group_query_id: int | None
    group_title: str | None
    user_id: int | None
    user: str | None