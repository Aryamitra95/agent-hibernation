from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/slow")
async def slow():
    await asyncio.sleep(2)
    return {"status": "done"}