from fastapi import FastAPI
from fastapi import File, UploadFile
from fastapi import HTTPException

app = FastAPI(title="Garment Defect Detection API", version="0.1.0")


@app.get("/", tags=["system"], summary="Root")
def root():
    return {"message": "Garment Defect Detection API is running"}


@app.get("/health", tags=["system"], summary="Health check")
def health_check():
    return {"status": "ok"}


@app.post("/detect-test", tags=["system"], summary="detect test")
async def detect_test(file: UploadFile = File(...)):
    if file.content_type.startswith("image/"):
        content = await file.read()
        return{"file_name" : file.filename,
                        "content_type" : file.content_type,
                        "size" : len(content)}
    else:
        raise HTTPException(status_code=400, detail="Only image files are allowed")
