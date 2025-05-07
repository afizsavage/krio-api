from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from models import Word, Definition, Example, Letter
from schemas import WordOut, WordCreateWithDetails
from db import get_db

router = APIRouter()

KRIO_DIGRAPHS = [
    "aw", "ay", "ch", "gb", "kp", "ny", "ɔy", "sh", "th", "zh"
]

@router.post("/", response_model=WordOut)
def create_word(payload: WordCreateWithDetails, db: Session = Depends(get_db)):
    word = payload.word.strip().lower()

    # Get the first 2 characters for possible digraph
    possible_digraph = word[:2]
    first_letter = word[:1]

    letter_char = possible_digraph if possible_digraph in KRIO_DIGRAPHS else first_letter

    # Look for the corresponding Letter
    letter = db.query(Letter).filter(Letter.character == letter_char).first()
    if not letter:
        raise HTTPException(status_code=404, detail=f"No matching letter found for '{letter_char}'")

    # Create the Word
    db_word = Word(word=word, letter_id=letter.id)
    db.add(db_word)
    db.commit()
    db.refresh(db_word)

    # Create the Definition
    db_definition = Definition(definition=payload.definition, word_id=db_word.id)
    db.add(db_definition)

    # Create the Example
    db_example = Example(example_text=payload.example_text, word_id=db_word.id)
    db.add(db_example)

    db.commit()
    return db_word

@router.get("/", response_model=List[WordOut])
def list_words(db: Session = Depends(get_db)):
    words = db.query(Word).all()
    return words
