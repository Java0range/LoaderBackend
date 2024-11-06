from fastapi import FastAPI
from pydantic import BaseModel
import db

app = FastAPI()


class Key(BaseModel):
    key: str


class Create(BaseModel):
    count: int


@app.get("/")
async def check_status():
    return {"msg": "true"}


@app.post("/auth/")
async def auth(key_inp: Key):
    if db.check_key(key_inp.key):
        return {"msg": "true"}
    else:
        return {"msg": "false"}


@app.post("/create/")
async def create_key(count_keys: Create):
    keys = db.create_keys(count_keys.count)
    return {"msg": keys}


@app.post("/clear/")
async def create_key():
    db.clear_db()