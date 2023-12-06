from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def html_response():
    return '<h1> Hello World! </h1>'

@app.get('/hello/{user}', response_class=HTMLResponse)
def hello_user(user:str):
    return f'<h1>Hello {user}</h1>'

@app.get('/bye/{user}', response_class=HTMLResponse)
def byes_user(user:str):
    return f'<h1>Bye {user}</h1>'

@app.get('/me/{user}', response_class=HTMLResponse)
def me(user:str):
    return f'<h1>I am {user}</h1>'
