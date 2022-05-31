from fastapi import FastAPI

app = FastAPI()
my_awesome_api = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}