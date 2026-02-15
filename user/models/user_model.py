from sqlalchemy import Column, Integer, String
from user.core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(127), nullable=False)
    email = Column(String(127), nullable=False, unique=True)
    password = Column(Integer(), nullable=False)
    role = Column(String(127), nullable=False)