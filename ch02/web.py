from fastapi import FastAPI

from ch02.data import get_champion

app = FastAPI()

@app.get("/champion")
def champion():
    return get_champion()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web:app", reload=True)
