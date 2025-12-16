from fastapi import FastAPI

app = FastAPI(title="Garment Defect Detection API", version="0.1.0")


@app.get("/", tags=["system"], summary="Root")
def root():
    return {"message": "Garment Defect Detection API is running"}


@app.get("/health", tags=["system"], summary="Health check")
def health_check():
    return {"status": "ok"}


@app.post("/detect-test", tags=["system"], summary="detect test")
def detect_test():
    return {"message": "detect endpoint reached"}
