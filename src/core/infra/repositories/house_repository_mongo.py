from core.infra.config.database import db, fs
from core.domain.entities import HouseModel
from fastapi import UploadFile


class MongoHouseRepository:
    def __init__(self):
        self.collection = db.house if db is not None else None

    def get_house_info(self, title: str) -> HouseModel:
        if self.collection is not None:
            house = self.collection.find_one({"title": title})
            if house:
                return HouseModel(
                    title=house["title"],
                    description=house["description"],
                    quote=house["quote"],
                    crest_url=house["crest_url"]
                )
        return None

    def upload_image(self, file: UploadFile):
        if self.collection is not None:
            file_id = fs.put(file.file, filename=file.filename,
                             content_type=file.content_type)
        return {"file_id": str(file_id)}
