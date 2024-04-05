from sqlalchemy import Boolean, Column, String, Integer

from src.core.db import Base


class Entity(Base):
    __tablename__ = "entities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String, nullable=False)
    has_deleted = Column(Boolean, default=False)
