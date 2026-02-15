from fastapi import HTTPException
from sqlalchemy.orm import Session
from user.models.user_model import User

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
    
def create_user(db: Session, name: str, email: str, role: str, password: str):
    if db.query(User).filter(User.email == email).first():
        return
    new_user = User(name=name, email=email, role=role, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db: Session,user_id: int, data: dict):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return 404
    if "email" in data and db.query(User).filter(User.email == data["email"]).first():
        return 400

    for field, value in data.items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return
    db.delete(db_user)
    db.commit()
    return {"message" : "User deleted..."}