from fastapi import FastAPI
from user.core.database import Base, engine
from user.router import user_router

app = FastAPI(title="User Manager")

app.include_router(user_router.router)

Base.metadata.create_all(bind=engine)