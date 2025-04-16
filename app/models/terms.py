from sqlalchemy import Column, BigInteger, String, Text, DateTime
from datetime import datetime
from app import db

class Term(db.Model):
    __tablename__ = 'terms'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"<Term id={self.id}, name='{self.name}', slug='{self.slug}'>"
