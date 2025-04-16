from datetime import datetime
from sqlalchemy import Column, String, BigInteger, DateTime
from sqlalchemy.orm import relationship

from app import db
from flask_login import UserMixin
from enum import Enum as UserEnum
class UserRole(UserEnum):
    ADMIN = 'admin'
    EDITOR = 'editor'
    AUTHOR = 'author'
    SUBSCRIBER = 'subscriber'

class UserStatus(UserEnum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    BANNED = 'banned'
# User model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(50),unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(db.Enum(UserRole), nullable=False, default=UserRole.SUBSCRIBER)
    status = Column(db.Enum(UserStatus), nullable=False, default=UserStatus.ACTIVE)
    created_at = Column(DateTime(), default=datetime.utcnow)
    meta = relationship('UserMeta', backref="user", uselist=False, cascade="all, delete-orphan", lazy=True)
    def __str__(self):
        return f"User( id = { self.id }, username = { self.username }, email = { self.email }, password = { self.password }, role = { self.role }, status = { self.status }, created_at = { self.created_at }, meta = { self.meta } )"