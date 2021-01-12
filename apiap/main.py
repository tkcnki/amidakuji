from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Param(BaseModel):
    Names: List[str] = []
    NumberInGroup: int

@app.get("/amida/{key}")
async def amida(key, param: Param):

    if key != "hJqDzsXImQOkU0fgiVnX":
        return {"message": "Hello World"}

    class Result(BaseModel):
        GroupName: str
        GroupMembers: List[str] = []

    result = Result(GroupName= "Group-1", GroupMembers= param.Names[0:4])

    return result


# samples

@app.get("/")
async def root():

    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/query/")
async def query_parameter(skip: int):
    return {"skip": skip}

class Item(BaseModel):
    name: str
    price: float

@app.post("/request/")
async def create_item(item: Item):
    return item