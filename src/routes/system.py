from fastapi import APIRouter
from fastapi import File, UploadFile
from src.utils.validation import validate_upload
from src.utils.decode import decode_image
from src.utils.grayscale import is_grayscale
from src.utils.metadata import extract_image_metadata

router = APIRouter(prefix="", tags=["system"])

@router.get("/", summary="Root")
def root():
    return {"message": "Garment Defect Detection API is running"}

@router.get("/health", summary="Health check")
def health_check():
    return {"status": "ok"}

@router.post("/detect-test", summary="detect test")
async def detect_test(file: UploadFile = File(...)):
        validate_upload(file)
        content = await file.read()
        img = decode_image(content)
        meta = extract_image_metadata(img)
        return {"file_name" : file.filename,
                "content_type" : file.content_type,
                "size" : len(content),
                **meta
                }
