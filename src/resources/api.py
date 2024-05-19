import numpy as np
from fastapi import FastAPI, HTTPException
from core.app.services import PredictHouseService
from core.infra import create_keras_model, UserResponseRequest
from core.domain.entities import HouseModel
from core.infra.repositories.house_repository_mongo import MongoHouseRepository

app = FastAPI()
model = create_keras_model()
predict_house_use_case = PredictHouseService(model)
house_repo = MongoHouseRepository()


houses = ['Grifinória', 'Sonserina', 'Corvinal', 'Lufa-Lufa']


@app.get("/")
def read_root():
    return {"message": "The Sorting Hat AI is running"}


@app.get("/house/{title}", response_model=HouseModel)
async def get_house(title: str):
    house = house_repo.get_house_info(title)
    if house:
        return house
    else:
        raise HTTPException(status_code=404, detail="House not found")


@app.post("/predict")
def predict(user_response: UserResponseRequest):
    house_index, probabilities = predict_house_use_case.predict(
        user_response.responses)
    return {"house": houses[house_index], "probabilities": probabilities.tolist()}


@app.post("/train")
def train(data: list, labels: list):
    predict_house_use_case.train_model(np.array(data), labels)
    return {"status": "training complete"}


@app.post("/evaluate")
def evaluate(data: list, labels: list):
    loss, accuracy = predict_house_use_case.evaluate_model(
        np.array(data), labels)
    return {"loss": loss, "accuracy": accuracy}
