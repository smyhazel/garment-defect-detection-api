from fastapi import APIRouter
from fastapi import HTTPException
import cv2
import numpy as np
from fastapi import File, UploadFile
from src.utils.validation import validate_upload
from src.utils.decode import decode_image
from src.utils.metadata import extract_image_metadata
from src.utils.decision import decide
from src.utils.scoring import compute_edge_score

router = APIRouter(prefix="", tags=["inference"])

@router.post("/detect", summary="detect")
async def detect(file: UploadFile = File(...)):
    validate_upload(file)
    content = await file.read()
    img = decode_image(content)
    if len(img.shape) == 3 and img.shape[2] == 3: 
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif len(img.shape) == 3 and img.shape[2] == 4:
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    else:
        gray_image = img
    score = compute_edge_score(gray_image)
    threshold = 0.08
    meta = extract_image_metadata(img)
    return {"file_name" : file.filename,
            "defect_score" : float(score),
            **decide(score, threshold),
            **meta
    }