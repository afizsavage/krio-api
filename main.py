# main.py
from fastapi import FastAPI
from db import Base, engine
from routers import letters  # once we add routers
from dotenv import load_dotenv

load_dotenv()  # This loads variables from .env

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(letters.router)  # once you implement it
