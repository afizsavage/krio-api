from pydantic import BaseModel
from typing import List, Optional


class LetterBase(BaseModel):
    character: str
    position: int
    is_digraph: bool = False

class LetterCreate(LetterBase):
    pass

class LetterOut(LetterBase):
    id: int
    class Config:
        orm_mode = True


class WordBase(BaseModel):
    title: str
    letter_id: int

class WordCreate(WordBase):
    pass

class WordOut(WordBase):
    id: int
    class Config:
        orm_mode = True


class TranslationBase(BaseModel):
    translation_text: str
    word_id: int

class TranslationCreate(TranslationBase):
    pass

class TranslationOut(TranslationBase):
    id: int
    class Config:
        orm_mode = True


class ExampleBase(BaseModel):
    example_text: str
    word_id: int

class ExampleCreate(ExampleBase):
    pass

class ExampleOut(ExampleBase):
    id: int
    class Config:
        orm_mode = True
