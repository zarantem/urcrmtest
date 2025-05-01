from modules.common.services import BaseService

from modules.groups.repository import GroupRepository

class GroupService(BaseService):
    def __init__(self, repository: GroupRepository):
        super().__init__(repository)