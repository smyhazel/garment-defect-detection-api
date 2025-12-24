import cv2
import numpy as np
from fastapi import HTTPException

def decode_image(content):
    np_arr = np.frombuffer(content, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise HTTPException(status_code=400, detail="Could not decode image")
    else:
        return img