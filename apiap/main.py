from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


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