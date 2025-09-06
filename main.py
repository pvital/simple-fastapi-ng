import os

import httpx
from fastapi import FastAPI

app = FastAPI()

pid = os.getpid()
print(pid)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/users/")
def read_users():
    headers = {
        "x-api-key": "reqres-free-v1",
    }
    resp = httpx.get("https://reqres.in/api/users", headers=headers)
    # print(resp)
    return resp.json()


@app.get("/users/{user_id}")
def read_user(user_id: int):
    headers = {
        "x-api-key": "reqres-free-v1",
    }
    resp = httpx.get(f"https://reqres.in/api/users/{user_id}", headers=headers)

    if resp.status_code != 200:
        return

    user = resp.json().get("data")
    return {
        "user_id": user.get("id", None),
        "email": user.get("email", None),
        "first_name": user.get("first_name", None),
        "last_name": user.get("last_name", None),
        "avatar": user.get("avatar", None),
    }
