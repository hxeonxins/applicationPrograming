import asyncio

import uvicorn
from fastapi import FastAPI, Body, Header

app = FastAPI()

#비동기 처리
@app.get("/async")
async def async_test():
    await asyncio.sleep(1)
    return {"hello": "async"}

#쿼리 매개변수
@app.post("/hi")
def greet(cost: str = Body(embed=True)):
    return f"진짜? {cost}원?"

#Header 반환
@app.post("/agent")
def get_agent(user_agent: str = Header()):
    return user_agent

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)