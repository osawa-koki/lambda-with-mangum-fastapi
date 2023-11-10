from fastapi import APIRouter

router = APIRouter()

@router.get("/api/ping", status_code=200)
async def root():
    return {"message": "Hello GET."}

@router.post("/api/ping", status_code=200)
async def root():
    return {"message": "Hello POST."}

@router.put("/api/ping", status_code=200)
async def root():
    return {"message": "Hello PUT."}

@router.delete("/api/ping", status_code=200)
async def root():
    return {"message": "Hello DELETE."}
