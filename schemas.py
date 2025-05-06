from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class LetterBase(BaseModel):
    character: str
    position: int
    is_digraph: bool = False

class LetterCreate(LetterBase):
    pass

class LetterOut(LetterBase):
    id: UUID

    class Config:
        orm_mode = True

class LetterUpdate(BaseModel):
    character: Optional[str] = None
    position: Optional[int] = None
    is_digraph: Optional[bool] = None


class WordBase(BaseModel):
    title: str
    letter_id: UUID

class WordCreate(WordBase):
    pass

class WordOut(WordBase):
    id: UUID

    class Config:
        orm_mode = True


class TranslationBase(BaseModel):
    translation_text: str
    word_id: UUID

class TranslationCreate(TranslationBase):
    pass

class TranslationOut(TranslationBase):
    id: UUID

    class Config:
        orm_mode = True


class ExampleBase(BaseModel):
    example_text: str
    word_id: UUID

class ExampleCreate(ExampleBase):
    pass

class ExampleOut(ExampleBase):
    id: UUID

    class Config:
        orm_mode = True
