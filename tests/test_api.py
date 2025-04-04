from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Iris Classifier API"}

def test_predict():
    # Test data with all values set to 0.0 to predict 'setosa'
    test_data = {
        "sepal_length": 0.0,
        "sepal_width": 0.0,
        "petal_length": 0.0,
        "petal_width": 0.0
    }
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert response.json()["prediction"] == "setosa"
