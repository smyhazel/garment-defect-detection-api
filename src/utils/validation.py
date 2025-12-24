from fastapi import HTTPException

def validate_upload(file):
    if file.content_type.startswith("image/"):
        return
    else:
        raise HTTPException(status_code=415, detail="Only image files are allowed")