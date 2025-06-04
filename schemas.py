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


class WordOut(BaseModel):
    id: UUID
    word: str
    letter_id: UUID  # <-- Add this if you want to return it
    class Config:
        orm_mode = True


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


# -------------------
# Definitions
# -------------------
class TranslationBase(BaseModel):
    translation: str
    word_id: UUID


class TranslationCreate(TranslationBase):
    pass

class TranslationOut(TranslationBase):
    id: UUID

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
    translation: TranslationOut

    class Config:
        orm_mode = True
 
class WordDetailsResponse(BaseModel):
    success: bool
    data: WordOutWithDetails

# -------------------
# Search Words
# -------------------
class SearchResponse(BaseModel):
    success: bool
    data: List[WordOut]