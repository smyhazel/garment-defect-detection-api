from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter(prefix="", tags=["inference"])

@router.post("/detect", summary="detect")
def detect():
    raise HTTPException(status_code=501, detail="Not implemented yet")