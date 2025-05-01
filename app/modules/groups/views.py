from modules.common.views import viewsets
from modules.groups.container import GroupContainer
from modules.groups.service import GroupService
from modules.groups.schemas import (
    GroupResponse,
    GroupCreate,
    GroupUpdateFull,
    GroupPartialUpdate
)

class GroupViewset(viewsets.ModelViewset):
    def __init__(self, container=None):
        self.container = container or GroupContainer()
        self._service = self.container.group_service()
        super().__init__(prefix="/groups", tags=['Groups'])
        self._setup_mixin_routes()

    @property
    def service(self) -> GroupService:
        return self._service

    @property
    def response_model(self):
        return GroupResponse

    @property
    def create_model(self):
        return GroupCreate

    @property
    def update_model(self):
        return GroupUpdateFull

    @property
    def partial_update_model(self):
        return GroupPartialUpdate