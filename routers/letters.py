from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from db import get_db
from models import Letter
from schemas import LetterCreate, LetterUpdate, LetterOut

router = APIRouter()

@router.post("", response_model=LetterOut)
def create_letter(letter: LetterCreate, db: Session = Depends(get_db)):
    db_letter = Letter(**letter.dict())
    db.add(db_letter)
    db.commit()
    db.refresh(db_letter)
    return db_letter

@router.get("", response_model=list[LetterOut])
def get_all_letters(db: Session = Depends(get_db)):
    return db.query(Letter).order_by(Letter.position).all()

@router.get("/{letter_id}", response_model=LetterOut)
def get_letter(letter_id: UUID, db: Session = Depends(get_db)):
    letter = db.query(Letter).get(letter_id)
    if not letter:
        raise HTTPException(status_code=404, detail="Letter not found")
    return letter

@router.put("/{letter_id}", response_model=LetterOut)
def update_letter(letter_id: UUID, update: LetterUpdate, db: Session = Depends(get_db)):
    letter = db.query(Letter).get(letter_id)
    if not letter:
        raise HTTPException(status_code=404, detail="Letter not found")
    for key, value in update.dict().items():
        setattr(letter, key, value)
    db.commit()
    db.refresh(letter)
    return letter

@router.delete("/{letter_id}")
def delete_letter(letter_id: UUID, db: Session = Depends(get_db)):
    letter = db.query(Letter).get(letter_id)
    if not letter:
        raise HTTPException(status_code=404, detail="Letter not found")
    db.delete(letter)
    db.commit()
    return {"detail": "Letter deleted"}
