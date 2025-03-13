import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
async def hello():
    return {"hello": "world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
