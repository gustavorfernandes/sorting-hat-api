from pydantic import BaseModel


class UserResponseRequest(BaseModel):
    responses: list