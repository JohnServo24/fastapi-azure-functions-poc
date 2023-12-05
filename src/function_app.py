import azure.functions as func
from fastapi import FastAPI
from controllers.todo_controller import todo_router

app = FastAPI()

app.include_router(todo_router, prefix="/todo", tags=["sample"])


function_app = func.AsgiFunctionApp(app=app, http_auth_level=func.AuthLevel.ANONYMOUS)
