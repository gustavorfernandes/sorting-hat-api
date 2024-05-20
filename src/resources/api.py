import numpy as np
from fastapi import FastAPI, File, UploadFile, HTTPException
from core.app.services import PredictHouseService
from core.infra import create_keras_model, UserResponseRequest
from core.infra.repositories.house_repository_mongo import MongoHouseRepository

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


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        predict_house_service.upload_image(file)
        return {"status": "success", "message": "File uploaded successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An error occurred: {str(e)}")
