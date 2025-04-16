from sqlalchemy import Column, String, BigInteger, Text, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db
from enum import Enum as PyEnum


class PostStatus(PyEnum):
    PUBLISH = 'publish'
    DRAFT = 'draft'
    PENDING = 'pending'
    PRIVATE = 'private'
    TRASH = 'trash'


class PostType(PyEnum):
    POST = 'post'
    PAGE = 'page'
    ATTACHMENT = 'attachment'


class Post(db.Model):
    __tablename__ = 'posts'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    excerpt = Column(Text, nullable=True)
    status = Column(Enum(PostStatus), nullable=False, default=PostStatus.DRAFT)
    type = Column(Enum(PostType), nullable=False, default=PostType.POST)

    author_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    author = relationship('User', backref='posts', lazy=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):
        return f"<Post id={self.id}, title='{self.title}', status='{self.status}', type='{self.type}'>"
