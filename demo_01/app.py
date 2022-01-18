from fastapi import FastAPI, Body
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class ReqLogin(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(req: ReqLogin = Body(...)):
    if req.username == "root" and req.password == "password":
        return {"success": True}
    return {"success": False}
