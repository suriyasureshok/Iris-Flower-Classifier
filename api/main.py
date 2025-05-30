from fastapi import FastAPI
from pydantic import BaseModel
from api.singleton_logger import LoggerSingleton
from api.singleton_model import Model_loader
import numpy as np

app = FastAPI()
logger = LoggerSingleton().logger
model =  Model_loader().model

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def root():
    return {"message": "Welcome to the Iris Flower Classifier API!"}

@app.post("/predict")
def predict_species(data: IrisData):
    logger.info(f"Received data: {data}")
    try:
        input_data = np.array([[data.sepal_length, data.sepal_width,
                                data.petal_length, data.petal_width]])
        prediction = model.predict(input_data)[0]
        logger.info(f"Prediction result: {prediction}")
        return {"predicted_class": prediction}
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        return {"error": str(e)}
