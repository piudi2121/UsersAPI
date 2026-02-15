from fastapi import FastAPI
from user.core.database import Base, engine
from user.router import user_router
from auth.routes import auth_router

app = FastAPI(title="User Manager")

app.include_router(user_router.router)
app.include_router(auth_router.auth_router)

Base.metadata.create_all(bind=engine)