from dependency_injector import containers, providers
from database import Database

from modules.projects.repository import ProjectRepository
from modules.projects.service import ProjectService

class ProjectContainer(containers.DeclarativeContainer):
    db = providers.Singleton(Database)
    
    project_repository = providers.Factory(
        ProjectRepository,
        db_session=db.provided.get_session
    )
    
    project_service = providers.Factory(
        ProjectService,
        repository=project_repository
    )