from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import os
from dotenv import load_dotenv
from config import settings

from model import train_model, predict_iris

# Load environment variables
load_dotenv()

# Get environment variables
MODEL_FILE = settings.MODEL_FILE
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Load the model
    if ENVIRONMENT == "production":
        # In production, always train a new model
        train_model(MODEL_FILE)
    else:
        # In development, only train if model doesn't exist
        if not os.path.exists(MODEL_FILE):
            train_model(MODEL_FILE)
    yield
    # Shutdown: Clean up if needed
    pass

# Create the FastAPI app instance with lifespan
app = FastAPI(title="Iris Classifier API", lifespan=lifespan)

# Define a Pydantic model for the request body
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Classifier API"}

@app.post("/predict")
def predict(features: IrisFeatures):
    # Convert the request data to a numpy array
    input_data = np.array([[features.sepal_length, features.sepal_width,
                             features.petal_length, features.petal_width]])
    try:
        prediction = predict_iris(input_data, MODEL_FILE)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# # Run the FastAPI app
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
