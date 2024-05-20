from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from core.domain.repositories import HouseRepository
from core.infra.pymongo import fs
from bson import ObjectId

common_router = APIRouter()
house_repo = HouseRepository()

@common_router.get("/")
def read_root():
    return {"message": "The Sorting Hat AI is running"}

@common_router.get("/image/{file_id}")
async def get_image(file_id: str):
    image_file = fs.get(ObjectId(file_id))
    if image_file:
        return StreamingResponse(image_file, media_type='image/jpg')
