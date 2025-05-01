from dependency_injector import containers, providers
from database import Database

from modules.tasks.repository import TaskRepository
from modules.tasks.service import TaskService

class TaskContainer(containers.DeclarativeContainer):
    db = providers.Singleton(Database)
    
    task_repository = providers.Factory(
        TaskRepository,
        db_session=db.provided.get_session
    )
    
    task_service = providers.Factory(
        TaskService,
        repository=task_repository
    )