from fastapi import APIRouter
from services import todo_services

todo_router = APIRouter()


@todo_router.get("/")
async def get_todo():
    return todo_services.get_todo()


@todo_router.post("/")
async def add_todo():
    return todo_services.add_todo()


@todo_router.delete("/{id}")
async def delete(id: str):
    return todo_services.delete_todo(id=id)


@todo_router.put("/{id}")
async def edit_todo(id: str):
    return todo_services.edit_todo(id=id)
