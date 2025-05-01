from modules.common.services import BaseService

from modules.projects.repository import ProjectRepository

class ProjectService(BaseService):
    def __init__(self, repository: ProjectRepository):
        super().__init__(repository)