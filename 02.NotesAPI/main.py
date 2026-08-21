from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from models import Note
from schema import NoteCreate, NoteUpdate, NoteResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/notes", response_model=NoteResponse)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    new_note = Note(
        title = note.title,
        content = note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

@app.get("/notes", response_model=list[NoteResponse])
def get_notes(db: Session = Depends(get_db)):
    notes = db.query(Note).all()

    return notes

@app.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note tidak ditemukan"
        )

    return note

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    existing_note = db.query(Note).filter(Note.id == note_id).first()

    if existing_note is None:
        raise HTTPException(
            status_code=404,
            detail="Note tidak ditemukan"
        )

    existing_note.title = note.title
    existing_note.content = note.content

    db.commit()
    db.refresh(existing_note)

    return existing_note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()

    if note is None:
        raise HTTPException(
            status_code=404,
            detail= "Note tidak ditemukan"
        )

    db.delete(note)
    db.commit()

    return {"message":"Note berhasil dihapus"}

@app.get("/search")
def search_notes(title: str, db: Session = Depends(get_db)):
    notes = db.query(Note).filter(Note.title.contains(title)).all()

    return notes