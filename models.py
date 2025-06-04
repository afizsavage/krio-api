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
    translation = relationship("Translation", back_populates="word", uselist=False, cascade="all, delete")
    examples = relationship("Example", back_populates="word", cascade="all, delete")


class Translation(Base):
    __tablename__ = "translations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    translation = Column(Text, nullable=False)
    word_id = Column(UUID(as_uuid=True), ForeignKey("words.id"), nullable=False)

    word = relationship("Word", back_populates="translation")


class Example(Base):
    __tablename__ = "examples"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    example = Column(Text, nullable=False)
    word_id = Column(UUID(as_uuid=True), ForeignKey("words.id"))

    word = relationship("Word", back_populates="examples")
