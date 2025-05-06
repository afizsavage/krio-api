from sqlalchemy import Column, BigInteger, Boolean, Integer, Text, CHAR, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Letter(Base):
    __tablename__ = "Letters"

    id = Column(BigInteger, primary_key=True, index=True)
    character = Column(CHAR(255), nullable=False)
    position = Column(Integer, nullable=False)
    is_digraph = Column(Boolean, nullable=False, default=False)

    words = relationship("Word", back_populates="letter")


class Word(Base):
    __tablename__ = "Words"

    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    letter_id = Column(BigInteger, ForeignKey("Letters.id"), nullable=False)

    letter = relationship("Letter", back_populates="words")
    translations = relationship("Translation", back_populates="word")
    examples = relationship("Example", back_populates="word")


class Translation(Base):
    __tablename__ = "Translations"

    id = Column(BigInteger, primary_key=True, index=True)
    translation_text = Column(Text, nullable=False)
    word_id = Column(BigInteger, ForeignKey("Words.id"), nullable=False)

    word = relationship("Word", back_populates="translations")


class Example(Base):
    __tablename__ = "Examples"

    id = Column(BigInteger, primary_key=True, index=True)
    example_text = Column(Text, nullable=False)
    word_id = Column(BigInteger, ForeignKey("Words.id"), nullable=False)

    word = relationship("Word", back_populates="examples")
