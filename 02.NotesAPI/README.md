# Notes API

A simple RESTful Notes API built with FastAPI, SQLite, and SQLAlchemy.

This project is a beginner backend mini project created to learn how to build an API with persistent data using a relational database.

## Features

- Create a note
- Get all notes
- Get a note by ID
- Update a note
- Delete a note
- Search notes by title
- Request validation with Pydantic
- Error handling with HTTPException
- SQLite database
- SQLAlchemy ORM
- Basic API testing with Pytest

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Pytest
- Uvicorn

## Project Structure

```text
Notes-API/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── test_main.py
├── requirements.txt
├── README.md
├── .gitignore
└── notes.db