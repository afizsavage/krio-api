from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


# -------------------
# Letters
# -------------------
class LetterBase(BaseModel):
    character: str
    position: int
    is_digraph: bool = False

class LetterCreate(LetterBase):
    pass

class LetterUpdate(BaseModel):
    character: Optional[str] = None
    position: Optional[int] = None
    is_digraph: Optional[bool] = None

class LetterOut(LetterBase):
    id: UUID

    class Config:
        orm_mode = True


# -------------------
# Words
# -------------------
class WordBase(BaseModel):
    word: str
    letter_id: UUID

class WordCreate(WordBase):
    pass

class WordOut(WordBase):
    id: UUID

    class Config:
        orm_mode = True


# -------------------
# Definitions
# -------------------
class DefinitionBase(BaseModel):
    definition: str
    word_id: UUID

class DefinitionCreate(DefinitionBase):
    pass

class DefinitionOut(DefinitionBase):
    id: UUID

    class Config:
        orm_mode = True


# -------------------
# Combined Word Creation
# -------------------
class DefinitionCreateWithExample(BaseModel):
    word: str
    definition: str
    example_text: str


# -------------------
# Examples
# -------------------
class ExampleBase(BaseModel):
    example_text: str
    word_id: UUID

class ExampleCreate(ExampleBase):
    pass

class ExampleOut(ExampleBase):
    id: UUID

    class Config:
        orm_mode = True
