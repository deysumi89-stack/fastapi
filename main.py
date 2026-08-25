from fastapi import FastAPI
from fastapi.param_functions import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "BUILDING FASTAPI"}

@app.get("/posts") # for retrieving data, the http method is GET
async def get_posts():
    return {"data": "This is first post"}

@app.post("/createposts") # for creating data, the http method is POST
async def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new post": f"title: {payload['title']}, content: {payload['content']}"}