from sqlalchemy import Column, BigInteger, String, Text, ForeignKey
from app import db
from sqlalchemy.orm import relationship

class PostMeta(db.Model):
    __tablename__ = 'post_meta'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    post_id = Column(BigInteger, ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)
    meta_key = Column(String(255), nullable=False)
    meta_value = Column(Text)

    post = relationship("Post", backref="meta", lazy=True)

    def __str__(self):
        return f"<PostMeta id={self.id}, post_id={self.post_id}, key='{self.meta_key}'>"
