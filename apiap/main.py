from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from random import shuffle
import time

app = FastAPI()

class Param(BaseModel):
    Names: List[str] = []
    NumberInGroup: int

Group_name_list = ["Alice", "Bob", "Carol", "Eve", "Peggy"]

@app.get("/amida/{key}")
async def amida(key, param: Param):

    # Key check
    if key != "hJqDzsXImQOkU0fgiVnX":
        time.sleep(3)
        return {"message": "Hello World"}

    len_names = len(param.Names)

    if len_names < Param.NumberInGroup:
        return {"message": "Ooops"}

    class Result(BaseModel):
        GroupName: str
        GroupMembers: List[str] = []

    if Param.NumberInGroup < 3 and 3 <= len_names <= 4 :
        return Result(GroupName = Group_name_list[0], GroupMembers = param.Names)

    shuffle(param.Names)


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