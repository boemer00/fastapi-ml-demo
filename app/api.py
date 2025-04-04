from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import os
from app.config import settings
from app.model import train_model, predict_iris

# Create the FastAPI app instance
app = FastAPI(title="Iris Classifier API")

# Define a Pydantic model for the request body
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Train model on startup if needed
@app.on_event("startup")
async def startup_event():
    model_path = os.path.join(settings.MODEL_DIR, settings.MODEL_FILENAME)
    if not os.path.exists(model_path):
        train_model(model_path)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Classifier API"}

@app.post("/predict")
def predict(features: IrisFeatures):
    # Convert the request data to a numpy array
    input_data = np.array([[features.sepal_length, features.sepal_width,
                             features.petal_length, features.petal_width]])
    try:
        model_path = os.path.join(settings.MODEL_DIR, settings.MODEL_FILENAME)
        prediction = predict_iris(input_data, model_path)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
