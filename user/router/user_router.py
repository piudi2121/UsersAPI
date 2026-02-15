from fastapi import APIRouter, Depends
from user.core.database import get_db
from user.schemas.user_schemas import UserResponse, UserCreate, UserUpdate
from sqlalchemy.orm import Session
from user.services import user_services

router = APIRouter(prefix="/users", tags=["User"])

@router.get('/{user_id}', response_model=UserResponse)
def get_user(user_id: int, db:Session = Depends(get_db)):
    return user_services.get_user(db=db, user_id=user_id)

@router.post('', response_model=UserResponse)
def create_user(user: UserCreate, db:Session = Depends(get_db)):
    return user_services.create_user(db, user.name, user.email, user.role, user.password)

@router.put('/{user_id}', response_model=UserResponse)
def update_user(user: UserUpdate, user_id: int, db:Session = Depends(get_db)):
    return user_services.update_user(db, user_id, user.model_dump(exclude_unset=True))

@router.delete('/{user_id}')
def delete_user(user_id: int, db:Session = Depends(get_db)):
    return user_services.delete_user(db, user_id)