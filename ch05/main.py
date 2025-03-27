from fastapi import FastAPI

from ch05.web import todo

app = FastAPI()
app.include_router(todo.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True, port=8000)
