from fastapi import FastAPI

app = FastAPI()


@app.get("/api-endpoint")
async def root():
    return {"message": "Hello World"}
