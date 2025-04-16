from sqlalchemy import Column, BigInteger, ForeignKey, PrimaryKeyConstraint
from app import db

class PostTermRelationship(db.Model):
    __tablename__ = 'post_term_relationships'

    object_id = Column(BigInteger, ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)
    term_taxonomy_id = Column(BigInteger, ForeignKey('term_taxonomy.id', ondelete='CASCADE'), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('object_id', 'term_taxonomy_id'),
    )

    def __str__(self):
        return f"<PostTermRelationship object_id={self.object_id}, term_taxonomy_id={self.term_taxonomy_id}>"
