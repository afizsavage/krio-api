from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from typing import List
from models import Example
from schemas import ExampleOut

router = APIRouter()

@router.get("/", response_model=List[ExampleOut])
def list_examples(db: Session = Depends(get_db)):
    examples = db.query(Example).all()
    return examples