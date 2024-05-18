import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from use_cases import PredictHouseUseCase
from frameworks_and_drivers import create_model

app = FastAPI()
model = create_model()
predict_house_use_case = PredictHouseUseCase(model)


class UserResponseRequest(BaseModel):
    responses: list


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
