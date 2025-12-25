from fastapi import FastAPI
from src.routes.system import router as system_router
from src.routes.inference import router as inference_router

app = FastAPI(title="Garment Defect Detection API", version="0.1.0")
app.include_router(system_router)
app.include_router(inference_router)
