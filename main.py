from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Here is the API response."}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

