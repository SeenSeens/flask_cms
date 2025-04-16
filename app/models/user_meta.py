from sqlalchemy import BigInteger, Column, ForeignKey, String, Text, UniqueConstraint
from app import db

class UserMeta(db.Model):
    __tablename__ = 'user_meta'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete="CASCADE"), unique=True, nullable=False)  # dùng string 'users.id'
    meta_key = Column(String(255), unique=True, nullable=False)
    meta_value = Column(Text, nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'meta_key', name='uq_user_meta'),
    )

    def __str__(self):
        return f"<UserMeta id={self.id}, user_id={self.user_id}, meta_key={self.meta_key}>"
