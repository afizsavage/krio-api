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
# Examples
# -------------------
class ExampleBase(BaseModel):
    example_text: str
    definition_id: UUID

class ExampleCreate(ExampleBase):
    definition_id: UUID

class ExampleOut(ExampleBase):
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
    examples: List[ExampleOut]


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


class WordOut(BaseModel):
    id: UUID
    word: str
    letter_id: UUID  # <-- Add this if you want to return it
    class Config:
        orm_mode = True

# -------------------
# Combined Word With Details
# -------------------
class WordCreateWithDetails(BaseModel):
    word: str
    definition_text: str  # consider renaming to definition_text for clarity
    example_text: str


class WordOutWithDetails(BaseModel):
    id: UUID
    word: str
    letter_id: UUID  # <-- Add this if you want to return it
    definitions: List[DefinitionOut]

    class Config:
        orm_mode = True
 
