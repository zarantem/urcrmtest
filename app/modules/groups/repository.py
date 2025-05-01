from modules.common.repositories import BaseRepository
from modules.groups.models import GroupModel

from sqlalchemy.ext.asyncio import AsyncSession

class GroupRepository(BaseRepository[GroupModel]):
    def __init__(self, db_session: AsyncSession):
        super(GroupRepository, self).__init__(GroupModel, db_session)