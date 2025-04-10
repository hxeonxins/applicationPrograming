from fastapi import FastAPI
from web import department as department_web
app = FastAPI()

app.include_router(department_web.router)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000)