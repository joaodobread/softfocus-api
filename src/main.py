from fastapi import FastAPI

app = FastAPI(
    title="Softfocus API",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
