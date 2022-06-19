from typing import Union

from fastapi import FastAPI, Path, Query, Header

app = FastAPI()

@app.get("/items/")
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}

@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(title="The ID of the item to get"), 
    s: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results