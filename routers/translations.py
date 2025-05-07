from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Word, Letter, Translation, Example
from schemas import TranslationCreateWithExample
from db import get_db

KRIO_DIGRAPHS = [
    "ch", "gb", "kp", "ng", "nj", "ny", "sh", "th"
]

router = APIRouter()

@router.post("/")
def create_translation(data: TranslationCreateWithExample, db: Session = Depends(get_db)):
    word_str = data.word.lower()
    first_two = word_str[:2]
    first_letter = word_str[0]

    # Determine the appropriate letter
    if first_two in KRIO_DIGRAPHS:
        letter = (
        db.query(Letter)
        .filter(func.lower(Letter.character) == first_two)
        .first()
    )
    else:
        letter = (
            db.query(Letter)
            .filter(func.lower(Letter.character) == first_letter)
            .first()
    )

    if not letter:
        raise HTTPException(status_code=400, detail="Matching letter not found for word.")

    # Check if word exists
    word = db.query(Word).filter(Word.title == word_str).first()
    if not word:
        word = Word(title=word_str, letter_id=letter.id)
        db.add(word)
        db.commit()
        db.refresh(word)

    # Create translation
    translation = Translation(translation_text=data.translation_text, word_id=word.id)
    db.add(translation)
    db.commit()
    db.refresh(translation)

    # Create example
    example = Example(example_text=data.example_text, translation_id=translation.id)
    db.add(example)
    db.commit()
    db.refresh(example)

    return {
        "word": word.title,
        "translation": translation.translation_text,
        "example": example.example_text,
    }
