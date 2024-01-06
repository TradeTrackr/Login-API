from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class Tradesman(Base):
    __tablename__ = 'tradesmen'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "hashed_password": self.hashed_password
        }