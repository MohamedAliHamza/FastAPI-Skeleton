from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.db import get_db
from src.app.models import Entity
from src.app.schema import CreateEntitySchema, GetEntitySchema
from src.app.services import get_entities, create_entity

router = APIRouter()


@router.get(
    "/", 
    status_code=status.HTTP_200_OK, 
    response_model=list[GetEntitySchema]
)
async def get_entities_endpoint(db: Session = Depends(get_db)):
    entities = await get_entities(db)
    return [
        GetEntitySchema(id=entity.id, value=entity.value)
        for entity in entities
    ]


@router.post(
    "/", 
    status_code=status.HTTP_201_CREATED, 
    response_model=GetEntitySchema
)
async def create_entity_endpoint(payload: CreateEntitySchema, db: Session = Depends(get_db)):
    entity = await create_entity(payload, db)
    return GetEntitySchema(id=entity.id, value=entity.value)
