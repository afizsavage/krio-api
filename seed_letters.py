from sqlalchemy.orm import Session
from db import SessionLocal
from models import Letter

# Krio alphabet (customize as needed)
krio_letters = [
    {"character": "a", "position": 1},
    {"character": "aw", "position": 2, "is_digraph": True},
    {"character": "ay", "position": 3, "is_digraph": True},
    {"character": "b", "position": 4},
    {"character": "ch", "position": 5, "is_digraph": True},
    {"character": "d", "position": 6},
    {"character": "e", "position": 7},
    {"character": "ɛ", "position": 8},
    {"character": "f", "position": 9},
    {"character": "g", "position": 10},
    {"character": "gb", "position": 11, "is_digraph": True},
    {"character": "h", "position": 12},
    {"character": "i", "position": 13},
    {"character": "j", "position": 14},
    {"character": "k", "position": 15},
    {"character": "kp", "position": 16, "is_digraph": True},
    {"character": "l", "position": 17},
    {"character": "m", "position": 18},
    {"character": "n", "position": 19},
    {"character": "ny", "position": 20, "is_digraph": True},
    {"character": "ŋ", "position": 21},
    {"character": "o", "position": 22},
    {"character": "ɔ", "position": 23},
    {"character": "ɔy", "position": 24, "is_digraph": True},
    {"character": "p", "position": 25},
    {"character": "r", "position": 26},
    {"character": "s", "position": 27},
    {"character": "sh", "position": 28, "is_digraph": True},
    {"character": "t", "position": 29},
    {"character": "th", "position": 30, "is_digraph": True},
    {"character": "u", "position": 31},
    {"character": "v", "position": 32},
    {"character": "w", "position": 33},
    {"character": "y", "position": 34},
    {"character": "z", "position": 35},
    {"character": "zh", "position": 36, "is_digraph": True}
]

def seed_letters():
    db: Session = SessionLocal()
    for entry in krio_letters:
        letter = Letter(**entry)
        db.add(letter)
    db.commit()
    db.close()
    print("✅ Letters seeded successfully.")

if __name__ == "__main__":
    seed_letters()
