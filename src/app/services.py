from models import Entity

from sqlalchemy.orm import Session


async def create_entity(entity: Entity) -> Entity:
    ...


async def get_entities(db: Session) -> list[Entity]:
    return db.query(Entity).filter(Entity.has_deleted == False).all()
