from pydantic import BaseModel


class HouseModel(BaseModel):
    title: str
    description: str
    quote: str
    crest_url_id: str
