# scripts/drop_all.py
from db import engine
from models import Base

Base.metadata.drop_all(bind=engine)
