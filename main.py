from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):

    if published:
        return {"data": f'{limit} published blogs from db'}
    else:
        return {"data": f'{limit} blogs from db'}


@app.get('/blog/unpublished')
def about():
    return {"status": "Unpublished"}


@app.get('/blog/{id}')
def about(id: int):
    return {"status": id}


@app.get('/blog/comment/{id}')
def about(id: int):
    return {"status": {"1", "2"}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {"data": f"blog is created with title as {request.title}"}
