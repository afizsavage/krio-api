from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from models import Word
from schemas import SearchResponse
from db import get_db

router = APIRouter()


@router.get("", response_model=SearchResponse)
def search_words(
    q: str = Query(..., min_length=1, description="Search term"),
    db: Session = Depends(get_db),
):
    # Search for words starting with the query
    results = db.query(Word).filter(Word.word.ilike(f"{q}%")).limit(5).all()
    return {"success": True, "data": results}
