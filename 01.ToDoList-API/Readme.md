# To-Do List API

Simple REST API untuk mengelola daftar tugas (to-do list), dibuat menggunakan **FastAPI**. Data disimpan sementara di memory (list Python) — belum menggunakan database, jadi data akan hilang setiap kali server di-restart.

## Fitur

- Menambah task baru
- Melihat semua task
- Mengubah task (title & status)
- Menghapus task

## Tech Stack

- Python
- FastAPI
- Uvicorn (ASGI server)

## Cara Menjalankan

1. Install dependency:
   ```bash
   pip install -r requirements.txt
   ```

2. Jalankan server:
   ```bash
   uvicorn main:app --reload
   ```

3. Buka dokumentasi API otomatis (Swagger UI) di browser:
   ```
   http://127.0.0.1:8000/docs
   ```

## Endpoint

| Method | Endpoint       | Deskripsi                    |
|--------|----------------|-------------------------------|
| GET    | `/tasks`       | Mengambil semua task          |
| POST   | `/tasks`       | Menambah task baru            |
| PUT    | `/tasks/{id}`  | Mengubah task berdasarkan ID  |
| DELETE | `/tasks/{id}`  | Menghapus task berdasarkan ID |

### Contoh Request — Tambah Task

```json
POST /tasks
{
  "title": "Belajar FastAPI"
}
```

### Contoh Response

```json
{
  "id": 1,
  "title": "Belajar FastAPI",
  "completed": false
}
```

## Struktur Project

```
01-todo-api-fastapi/
├── README.md
├── main.py
└── requirements.txt
```

## Catatan

Data disimpan di dalam memori (list Python), sehingga akan hilang ketika server di-restart. Project ini dibuat sebagai latihan sebelum mempelajari SQLite, SQLAlchemy, dan database persistence.

Pembelajaran yang didapat:

- Merancang endpoint CRUD
- Menggunakan Pydantic untuk validasi data
- Mencari data berdasarkan ID
- Menggunakan helper function untuk mengurangi duplikasi kode
- Memahami perbedaan ID dan index pada list
- Memahami konsep object reference pada list dan dictionary Python

Project ini merupakan bagian dari roadmap belajar backend Python dan FastAPI.