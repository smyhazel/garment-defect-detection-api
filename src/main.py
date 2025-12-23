from fastapi import FastAPI
from fastapi import File, UploadFile
from fastapi import HTTPException
import cv2
import numpy as np

app = FastAPI(title="Garment Defect Detection API", version="0.1.0")


@app.get("/", tags=["system"], summary="Root")
def root():
    return {"message": "Garment Defect Detection API is running"}


@app.get("/health", tags=["system"], summary="Health check")
def health_check():
    return {"status": "ok"}

def is_grayscale(img):
    if (len(img.shape) == 2) or (len(img.shape) == 3 and img.shape[2] == 1):
        return True
    else:
        return False
    
def decode_image(content):
    np_arr = np.frombuffer(content, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise HTTPException(status_code=400, detail="Could not decode image")
    else:
        return img
    
def extract_image_metadata(img):
    h, w = img.shape[:2]
    channels = 1 if len(img.shape) == 2 else img.shape[2] 
    is_gray = is_grayscale(img)
    return {"width" : w,
            "height" : h,
            "channels" : channels,
            "is_grayscale": is_gray} 

@app.post("/detect-test", tags=["system"], summary="detect test")
async def detect_test(file: UploadFile = File(...)):
    if file.content_type.startswith("image/"):
        content = await file.read()
        img = decode_image(content)
        metadata = extract_image_metadata(img)
        return {"file_name" : file.filename,
                "content_type" : file.content_type,
                "size" : len(content),
                **metadata
                }
    else:
        raise HTTPException(status_code=400, detail="Only image files are allowed")

@app.post("/detect", tags=["inference"], summary="detect")
def detect():
    raise HTTPException(status_code=501, detail="Not implemented yet")
