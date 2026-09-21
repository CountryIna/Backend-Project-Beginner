# To-Do List API

A simple REST API for managing a to-do list, built with **FastAPI**. Data is stored temporarily in memory (a Python list), so there is no database yet and all data is lost whenever the server restarts.

## Features

- Add a new task
- View all tasks
- Update a task (title & status)
- Delete a task

## Tech Stack

- Python
- FastAPI
- Uvicorn (ASGI server)

## Getting Started

1. Install dependencies:
```bash
   pip install -r requirements.txt
```

2. Run the server:
```bash
   uvicorn main:app --reload
```

3. Open the automatic API documentation (Swagger UI) in your browser:
```
   http://127.0.0.1:8000/docs
```

## Endpoints

| Method | Endpoint       | Description                |
|--------|----------------|----------------------------|
| GET    | `/tasks`       | Get all tasks              |
| POST   | `/tasks`       | Add a new task             |
| PUT    | `/tasks/{id}`  | Update a task by ID        |
| DELETE | `/tasks/{id}`  | Delete a task by ID        |

### Example Request — Add a Task

```json
POST /tasks
{
  "title": "Learn FastAPI"
}
```

### Example Response

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

## Project Structure

```
01-todo-api-fastapi/
├── README.md
├── main.py
└── requirements.txt
```

## Notes

Data is stored in memory (a Python list), so it is lost when the server restarts. This project was built as practice before learning SQLite, SQLAlchemy, and database persistence.

What I learned:

- Designing CRUD endpoints
- Using Pydantic for data validation
- Finding data by ID
- Using helper functions to reduce code duplication
- Understanding the difference between an ID and a list index
- Understanding the concept of object references in Python lists and dictionaries

This project is part of my Python and FastAPI backend learning roadmap.