from sqlalchemy import Column, BigInteger, String, Text
from app import db

class Option(db.Model):
    __tablename__ = 'options'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    option_key = Column(String(255), unique=True, nullable=False)
    option_value = Column(Text, nullable=False)

    def __str__(self):
        return f"<Option key={self.option_key}, value={self.option_value}>"
