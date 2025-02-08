from sqlalchemy.orm import Session
from database import Base, engine
from sqlalchemy import Column, Integer, String

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)

Base.metadata.create_all(bind=engine)
