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
    return JSONResponse(
        status_code=500,
        content={
            "error": "InternalServerException",
            "message": "The system encountered a simulated error for SRE testing.",
            "trace_id": "SRE-TEST-12345",
            "suggestion": "Check the Azure Dashboard for metric spikes."
        }
    )