from modules.common.repositories import BaseRepository
from modules.projects.models import ProjectModel

from sqlalchemy.ext.asyncio import AsyncSession

class ProjectRepository(BaseRepository[ProjectModel]):
    def __init__(self, db_session: AsyncSession):
        super(ProjectRepository, self).__init__(ProjectModel, db_session)