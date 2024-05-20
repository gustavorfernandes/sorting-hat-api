import os
from core.infra.pymongo.database_connection import db
from core.domain.models import HouseModel
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("BASE_URL")


class HouseRepository:
    def __init__(self):
        self.collection = db.house if db is not None else None

    def get_house_info(self, title: str) -> HouseModel:
        if self.collection is not None:
            house = self.collection.find_one({"title": title})
            if house:
                crest_url = None
                file_id = house.get("crest_url_id")
                if file_id:
                    crest_url = f"{base_url}/image/{file_id}"
                return HouseModel(
                    title=house["title"],
                    description=house["description"],
                    quote=house["quote"],
                    crest_url=crest_url
                )
        return None
