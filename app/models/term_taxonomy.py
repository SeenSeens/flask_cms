from sqlalchemy import Column, BigInteger, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class TermTaxonomy(db.Model):
    __tablename__ = 'term_taxonomy'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    term_id = Column(BigInteger, ForeignKey('terms.id', ondelete='CASCADE'), nullable=False)
    taxonomy = Column(Enum('terms', 'tag', 'product_cat', 'product_tag', 'product_brand'), nullable=False)
    parent = Column(BigInteger, ForeignKey('term_taxonomy.id', ondelete='SET NULL'), nullable=True)
    count = Column(BigInteger, nullable=False, default=0)

    # Relationships
    term = relationship("Term", backref="taxonomies", lazy=True)
    children = relationship("TermTaxonomy", backref=db.backref("parent_term", remote_side=[id]), lazy=True)

    def __str__(self):
        return f"<TermTaxonomy id={self.id}, taxonomy='{self.taxonomy}', term_id={self.term_id}, parent={self.parent}>"
