import os

import httpx
import instana  # noqa: F401
from fastapi import FastAPI

app = FastAPI()

pid = os.getpid()
print(pid)

api_url = "https://jsonplaceholder.typicode.com"


@app.get("/")
def read_root():
    return {"message": "Hello from Instana World"}


@app.get("/users/")
def read_users():
    headers = {
        "Content-type": "application/json; charset=UTF-8",
    }
    resp = httpx.get(f"{api_url}/users", headers=headers)
    # print(resp)
    return resp.json()


@app.get("/users/{user_id}")
def read_user(user_id: int):
    headers = {
        "Content-type": "application/json; charset=UTF-8",
    }
    resp = httpx.get(f"{api_url}/users/{user_id}", headers=headers)

    if resp.status_code != 200:
        return

    user = resp.json()
    return {
        "user_id": user.get("id", None),
        "email": user.get("email", None),
        "name": user.get("name", None),
        "username": user.get("username", None),
        "website": user.get("website", None),
    }
