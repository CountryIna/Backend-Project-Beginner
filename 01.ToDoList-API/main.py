from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
tasks = []

class Task(BaseModel):
    title : str

next_id = 1

#MENCARI DATA MENGGUNAKAN ID
def find_task_by_id(id: int):
    for item in tasks:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="ID Task tidak ditemukan")

#MEMBACA
@app.get("/tasks")
def get_tasks():
    return tasks

#MENAMBAH
@app.post("/tasks")
def create_task(task: Task):
    global next_id

    new_task = {"id": next_id,
                 "title":task.title,
                 "completed":False}
    tasks.append(new_task)
    next_id += 1
    return new_task

#MENGEDIT
@app.put("/tasks/{id}")
def update_task(id: int, task: Task):
    task_item = find_task_by_id(id)
    task_item["title"] = task.title
    task_item["completed"] = True
    return task_item

#MENGHAPUS
@app.delete("/tasks/{id}")
def delete_task(id: int):
    task_item = find_task_by_id(id)
    tasks.remove(task_item)
    return {"message":"Task berhasil di hapus"}