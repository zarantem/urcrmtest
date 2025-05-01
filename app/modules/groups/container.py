from dependency_injector import containers, providers
from database import Database

from modules.groups.repository import GroupRepository
from modules.groups.service import GroupService

class GroupContainer(containers.DeclarativeContainer):
    db = providers.Singleton(Database)
    
    user_repository = providers.Factory(
        GroupRepository,
        db_session=db.provided.get_session
    )
    
    user_service = providers.Factory(
        GroupService,
        repository=user_repository
    )