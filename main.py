# main.py
from fastapi import FastAPI
from db import Base, engine
from routers import all_routers
from dotenv import load_dotenv

load_dotenv()  # This loads variables from .env

app = FastAPI(
    title="Krio Dictionary API",
    version="1.0.0",
    description="API for managing Krio dictionary data including letters, words, translations, and examples."
)

Base.metadata.create_all(bind=engine)

# Register each router
for router, prefix, tags in all_routers:
    app.include_router(router, prefix=f"/api{prefix}", tags=tags)

@app.get("/")
def root():
    return {"message": "Welcome to the Krio Dictionary API!"}