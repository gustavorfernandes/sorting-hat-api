import numpy as np
from fastapi import FastAPI
from core.app.services.predict_house import PredictHouseService
from core.infra.keras_model import create_keras_model
from core.infra.pydantic_base_model import UserResponseRequest

app = FastAPI()
model = create_keras_model()
predict_house_use_case = PredictHouseService(model)


houses = ['Grifinória', 'Sonserina', 'Corvinal', 'Lufa-Lufa']


@app.get("/")
def read_root():
    return {"message": "The Sorting Hat AI is running"}


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
