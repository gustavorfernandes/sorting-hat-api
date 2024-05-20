import numpy as np
from keras.api.utils import to_categorical
from core.infra.repositories.house_repository_mongo import MongoHouseRepository
from core.domain.entities import HouseModel


house_repo = MongoHouseRepository()
houses = ['griffindor', 'slytherin', 'ravenclaw', 'hufflepuff']


class PredictHouseService:
    def __init__(self, model):
        self.model = model

    def train_model(self, data, labels, epochs=50, batch_size=8):
        labels = to_categorical(labels, num_classes=4)
        self.model.fit(data, labels, epochs=epochs, batch_size=batch_size)

    def evaluate_model(self, data, labels):
        labels = to_categorical(labels, num_classes=4)
        loss, accuracy = self.model.evaluate(data, labels)
        return loss, accuracy

    def predict(self, new_responses) -> HouseModel:
        prediction = self.model.predict(np.array([new_responses]))
        house_index = np.argmax(prediction)

        return house_repo.get_house_info(houses[house_index])

    def upload_image(self, file):
        return house_repo.upload_image(file)
