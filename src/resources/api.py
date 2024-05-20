import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from core.app.services import PredictHouseService
from core.infra import create_keras_model, UserResponseRequest
from core.infra.repositories.house_repository_mongo import MongoHouseRepository
from core.infra.config.database import fs
from bson import ObjectId

app = FastAPI()
model = create_keras_model()
predict_house_service = PredictHouseService(model)
house_repo = MongoHouseRepository()


@app.get("/")
def read_root():
    return {"message": "The Sorting Hat AI is running"}


@app.post("/predict")
def predict(user_response: UserResponseRequest):
    return predict_house_service.predict(
        user_response.responses)


@app.post("/train")
def train(data: list, labels: list):
    predict_house_service.train_model(np.array(data), labels)
    return {"status": "training complete"}


@app.post("/evaluate")
def evaluate(data: list, labels: list):
    loss, accuracy = predict_house_service.evaluate_model(
        np.array(data), labels)
    return {"loss": loss, "accuracy": accuracy}


@app.get("/image/{file_id}")
async def get_image(file_id: str):
    image_file = fs.get(ObjectId(file_id))
    if image_file:
        return StreamingResponse(image_file, media_type='image/jpg')
