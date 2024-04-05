from pydantic import BaseModel


class BaseEntitySchema(BaseModel):
    value: str


class CreateEntitySchema(BaseEntitySchema):
    pass


class GetEntitySchema(BaseEntitySchema):
    id: int
    