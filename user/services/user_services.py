from fastapi import HTTPException
from user.repository import user_repository
from sqlalchemy.orm import Session

def get_user(db: Session, user_id: int):
    user = user_repository.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
    
def create_user(db: Session, name: str, email: str, role: str, password: str):
    user = user_repository.create_user(db=db, name=name, email=email, role=role, password=password)
    if not user:
        raise HTTPException(status_code=400, detail="User already exists")
    return user

def update_user(db: Session, user_id: int, data: dict):
    print(data)
    user = user_repository.update_user(db, user_id=user_id, data=data)
    if user == 404:
        raise HTTPException(status_code=404, detail='User does not exists')
    elif user == 400:
        raise HTTPException(status_code=400, detail="Email already used")
    return user

def delete_user(db: Session, user_id: int):
    msg = user_repository.delete_user(db, user_id=user_id)
    if not msg:
        raise HTTPException(status_code=404, detail='User does not exists')
    return msg