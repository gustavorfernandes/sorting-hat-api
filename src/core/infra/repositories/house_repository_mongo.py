from core.infra.config.database import db
from core.domain.entities import House, HouseModel


class MongoHouseRepository:
    def __init__(self):
        self.collection = db.houses if db else None

    def add_house(self, house: House):
        if self.collection:
            self.collection.insert_one({
                "title": house.title,
                "description": house.description,
                "quote": house.quote,
                "crest_url": house.crest_url
            })

    def get_house_info(self, title: str) -> HouseModel:
        if self.collection:
            house = self.collection.find_one({"title": title})
            if house:
                return HouseModel(
                    title=house["title"],
                    description=house["description"],
                    quote=house["quote"],
                    crest_url=house["crest_url"]
                )
        return None
