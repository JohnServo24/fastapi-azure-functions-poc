async def get_todo():
    return {"info": "Get todo"}


async def add_todo():
    return {"info": "Add todo"}


async def delete_todo(id: str):
    return {"info": "Delete todo", "id": id}


async def edit_todo(id: str):
    return {"info": "Edit todo", "id": id}
