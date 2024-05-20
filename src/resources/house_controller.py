import numpy as np
from fastapi import APIRouter
from core.app.services import HouseService
from core.infra.pydantic import UserResponseRequest
from core.infra.keras import create_keras_model
from core.domain.repositories import HouseRepository

house_router = APIRouter()
keras_model = create_keras_model()
house_service = HouseService(keras_model)
house_repo = HouseRepository()


@house_router.post("/predict")
def predict(user_response: UserResponseRequest):
    return house_service.predict(
        user_response.responses)


@house_router.post("/train")
def train(data: list, labels: list):
    house_service.train_model(np.array(data), labels)
    return {"status": "training complete"}


@house_router.post("/evaluate")
def evaluate(data: list, labels: list):
    loss, accuracy = house_service.evaluate_model(
        np.array(data), labels)
    return {"loss": loss, "accuracy": accuracy}
