from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from uuid import UUID
from datetime import date
import random

from models import Word, Translation, Example, Letter
from schemas import WordOut, WordCreateWithDetails, WordOutWithDetails, WordDetailsResponse
from db import get_db

router = APIRouter()

KRIO_DIGRAPHS = [
    "aw", "ay", "ch", "gb", "kp", "ny", "ɔy", "sh", "th", "zh"
]

@router.post("", response_model=WordOut, status_code=status.HTTP_201_CREATED)
def create_word(payload: WordCreateWithDetails, db: Session = Depends(get_db)):
    word = payload.word.strip().lower()

    # Get the correct letter character based on digraph rules
    possible_digraph = word[:2]
    first_letter = word[:1]
    letter_char = possible_digraph if possible_digraph in KRIO_DIGRAPHS else first_letter

    # Fetch matching letter from DB
    letter = db.query(Letter).filter(Letter.character == letter_char).first()
    if not letter:
        raise HTTPException(status_code=404, detail=f"No matching letter found for '{letter_char}'")

    try:
        # Create the Word
        db_word = Word(word=word, letter_id=letter.id)
        db.add(db_word)
        db.flush()  # Assigns db_word.id

        # Create the Definition
        db_definition = Translation(definition=payload.definition_text, word_id=db_word.id)
        db.add(db_definition)
        db.flush()  # Assigns db_definition.id

        # Create the Example
        db_example = Example(example_text=payload.example_text, definition_id=db_definition.id)
        db.add(db_example)

        db.commit()
        db.refresh(db_word)

        return db_word

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating word: {str(e)}")

@router.get("", response_model=List[WordOut])
def list_words(db: Session = Depends(get_db)):
    words = db.query(Word).all()
    return words

# Get words by letter_ID
@router.get("/letter/{letter_id}", response_model=List[WordOut])
def get_words_by_letter(letter_id: UUID, db: Session = Depends(get_db)):
    words = db.query(Word).filter(Word.letter_id == letter_id).all()
    return words

@router.get("/word-of-the-day", response_model=WordOutWithDetails)
def word_of_the_day(db: Session = Depends(get_db)):
    # Use today's date as a seed to get a consistent word every day
    today = date.today()
    random.seed(today.toordinal())

    total_words = db.query(Word).count()
    if total_words == 0:
        raise HTTPException(status_code=404, detail="No words available.")

    offset = random.randint(0, total_words - 1)
    word = db.query(Word).offset(offset).first()

    return word

@router.get("/{word_id}", response_model=WordDetailsResponse)
def get_word(word_id: UUID, db: Session = Depends(get_db)):
    word = db.query(Word).get(word_id)
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")
    return {"success": True, "data": word}