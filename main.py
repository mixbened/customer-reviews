from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/item")
def read_item(item: Item):
    return {"item_sent": item, }