from modules.common.views import viewsets
from modules.tasks.container import TaskContainer
from modules.tasks.service import TaskService
from modules.tasks.schemas import (
    TaskResponse,
    TaskCreate,
    TaskUpdateFull,
    TaskPartialUpdate
)

class TaskViewset(viewsets.ModelViewset):
    def __init__(self, container=None):
        self.container = container or TaskContainer()
        self._service = self.container.task_service()
        super().__init__(prefix="/tasks", tags=['Tasks'])
        self._setup_mixin_routes()

    @property
    def service(self) -> TaskService:
        return self._service

    @property
    def response_model(self):
        return TaskResponse

    @property
    def create_model(self):
        return TaskCreate

    @property
    def update_model(self):
        return TaskUpdateFull

    @property
    def partial_update_model(self):
        return TaskPartialUpdate