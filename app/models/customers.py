from sqlalchemy import Column, BigInteger, String, Text, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app import db

class Customer(db.Model):
    __tablename__ = 'customers'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user = relationship('User', backref='customers')

    def __str__(self):
        return f"<Customer name={self.name}, email={self.email}>"
