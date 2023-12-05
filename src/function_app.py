import azure.functions as func
from fastapi import FastAPI

fastapi_app = FastAPI()


@fastapi_app.get("/sample")
async def index():
    return {
        "info": "Try /hello/john for parameterized route.",
    }


@fastapi_app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }


app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)
