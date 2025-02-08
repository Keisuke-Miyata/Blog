from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Post

router = APIRouter(prefix="/posts", tags=["Posts"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

@router.post("/")
def create_post(title: str, content: str, db: Session = Depends(get_db)):
    new_post = Post(title=title, content=content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
