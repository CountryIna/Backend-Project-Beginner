# Short URL

A simple URL shortener API built with Flask and SQLite.

This project is a beginner backend mini project created to learn how to build a REST API with persistent data and redirects.

## Features

- Create a short URL from a long URL
- Random 6-character unique code
- URL validation (http and https only)
- Redirect to the original URL
- Click counter
- Statistics for each short URL
- Error handling with JSON responses
- SQLite database

## Tech Stack

- Python
- Flask
- SQLite

## Getting Started

```bash
pip install flask
python app.py
```

The server runs at `http://127.0.0.1:5000`.

## API Endpoints

| Method | Endpoint        | Description                     |
|--------|-----------------|---------------------------------|
| POST   | `/shorten`      | Create a short URL              |
| GET    | `/<code>`       | Redirect to the original URL    |
| GET    | `/<code>/stats` | Get clicks and creation date    |

