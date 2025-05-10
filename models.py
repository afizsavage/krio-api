import uuid
from sqlalchemy import Column, Text, Boolean, Integer, CHAR, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Letter(Base):
    __tablename__ = "letters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = Column(CHAR(255), nullable=False)
    position = Column(Integer, nullable=False)
    is_digraph = Column(Boolean, nullable=False, default=False)

    words = relationship("Word", back_populates="letter", cascade="all, delete")


class Word(Base):
    __tablename__ = "words"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    word = Column(Text, nullable=False)
    letter_id = Column(UUID(as_uuid=True), ForeignKey("letters.id"), nullable=False)

    letter = relationship("Letter", back_populates="words")
    definitions = relationship("Definition", back_populates="word", cascade="all, delete")


class Definition(Base):
    __tablename__ = "definitions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    definition = Column(Text, nullable=False)
    word_id = Column(UUID(as_uuid=True), ForeignKey("words.id"), nullable=False)

    word = relationship("Word", back_populates="definitions")
    examples = relationship("Example", back_populates="definition", cascade="all, delete")



class Example(Base):
    __tablename__ = "examples"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    example_text = Column(Text, nullable=False)
    definition_id = Column(UUID(as_uuid=True), ForeignKey("definitions.id"))
    
    definition = relationship("Definition", back_populates="examples")
