from modules.common.repositories import BaseRepository
from modules.tasks.models import TaskModel

from sqlalchemy.ext.asyncio import AsyncSession

class TaskRepository(BaseRepository[TaskModel]):
    def __init__(self, db_session: AsyncSession):
        super(TaskRepository, self).__init__(TaskModel, db_session)