from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, EmailStr
from typing import Optional, List


app = FastAPI(title="Integration with SQL")

engine = create_engine("sqlite:///users.db", connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(127), nullable=False)
    email = Column(String(127), nullable=False, unique=True)
    role = Column(String(127), nullable=False)


Base.metadata.create_all(engine)

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    role: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/users/{user_id}', response_model=UserResponse)
def get_user(user_id:int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User does not exists')
    return user


@app.post('/users/', response_model=UserResponse)
def create_user(user: UserCreate, db:Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="User already exists")
    
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.put('/users/{user_id}', response_model=UserResponse)
def update_user(user_id:int, user:UserUpdate, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail='User does not exists')
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already used")
    
    for field, value in user.model_dump(exclude_unset=True).items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete('/users/{user_id}')
def delete_user(user_id:int, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail='User does not exists')

    db.delete(db_user)
    db.commit()
    return {"message" : "User deleted..."}


@app.get('/users/', response_model=List[UserResponse])
def get_all_users(db:Session = Depends(get_db)):
    return db.query(User).all()