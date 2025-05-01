from modules.common.views import viewsets
from modules.projects.container import ProjectContainer
from modules.projects.service import ProjectService
from modules.projects.schemas import (
    ProjectResponse,
    ProjectCreate,
    ProjectUpdateFull,
    ProjectPartialUpdate
)

class ProjectViewset(viewsets.ModelViewset):
    def __init__(self, container=None):
        self.container = container or ProjectContainer()
        self._service = self.container.project_service()
        super().__init__(prefix="/projects", tags=['Projects'])
        self._setup_mixin_routes()

    @property
    def service(self) -> ProjectService:
        return self._service

    @property
    def response_model(self):
        return ProjectResponse

    @property
    def create_model(self):
        return ProjectCreate

    @property
    def update_model(self):
        return ProjectUpdateFull

    @property
    def partial_update_model(self):
        return ProjectPartialUpdate