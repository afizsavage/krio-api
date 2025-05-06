from sqlalchemy.orm import Session
from db import SessionLocal
from models import Letter

# Krio alphabet (customize as needed)
krio_letters = [
    {"character": "A", "position": 1},
    {"character": "Aw", "position": 2, "is_digraph": True},
    {"character": "Ay", "position": 3, "is_digraph": True},
    {"character": "B", "position": 4},
    {"character": "Ch", "position": 5, "is_digraph": True},
    {"character": "D", "position": 6},
    {"character": "E", "position": 7},
    {"character": "Ɛ", "position": 8},  
    {"character": "F", "position": 9},
    {"character": "G", "position": 10},
    {"character": "Gb", "position": 11, "is_digraph": True},
    {"character": "H", "position": 12},
    {"character": "I", "position": 13},
    {"character": "J", "position": 14},
    {"character": "K", "position": 15},
    {"character": "Kp", "position": 16,"is_digraph": True},
    {"character": "L", "position": 17},
    {"character": "M", "position": 18},
    {"character": "N", "position": 19},
    {"character": "Ny", "position": 20, "is_digraph": True},
    {"character": "Ŋ", "position": 21},
    {"character": "O", "position": 22},
    {"character": "Ɔ", "position": 23,},
    {"character": "Ɔy", "position": 24,"is_digraph": True},
    {"character": "P", "position": 25},
    {"character": "R", "position": 26},
    {"character": "S", "position": 27},
    {"character": "Sh", "position": 28,"is_digraph": True},
    {"character": "T", "position": 29},
    {"character": "Th", "position": 30,"is_digraph": True},
    {"character": "U", "position": 31},
    {"character": "V", "position": 32},
    {"character": "W", "position": 33},
    {"character": "Y", "position": 34},
    {"character": "Z", "position": 35},
    {"character": "Zh", "position": 36}
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
