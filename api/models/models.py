from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime, func
from sqlalchemy.orm import relationship

from api.database import Base
from api.models.user_form import SubjectTypeEnum, SubjectStatusEnum


class BaseSQL(Base):
    __abstract__ = True

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)


class Task(BaseSQL):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, unique=True)
    subject_id = Column(Integer)
    subject_type = Column(Enum(SubjectTypeEnum))
    status = Column(Enum(SubjectStatusEnum))
    details = Column(String)


class User(BaseSQL):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    token = Column(String, unique=True)

