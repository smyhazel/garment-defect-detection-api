from fastapi import FastAPI
from fastapi import HTTPException
from src.routes.system import router as system_router

app = FastAPI(title="Garment Defect Detection API", version="0.1.0")
app.include_router(system_router)

@app.post("/detect", tags=["inference"], summary="detect")
def detect():
    raise HTTPException(status_code=501, detail="Not implemented yet")
