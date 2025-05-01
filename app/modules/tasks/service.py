from modules.common.services import BaseService

from modules.tasks.repository import TaskRepository

class TaskService(BaseService):
    def __init__(self, repository: TaskRepository):
        super().__init__(repository)