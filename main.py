# main.py
from fastapi import FastAPI
from db import Base, engine
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from routers import all_routers


load_dotenv()  # This loads variables from .env

app = FastAPI(
    title="Krio Dictionary API",
    version="1.0.0",
    description="API for managing Krio dictionary data including letters, words, translations, and examples."
)

Base.metadata.create_all(bind=engine)

# Register each router
for router, prefix, tags in all_routers:
    app.include_router(router, prefix=f"/api/v1{prefix}", tags=tags)

# Add CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Krio Dictionary API!"}