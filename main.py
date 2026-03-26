from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Here is the API response."}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/error")
async def error_check():
    return {"status": "unhealthy"}
    raise HTTPException(status_code=500, detail="The system has encountered a critical failure!")