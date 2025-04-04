# FastAPI ML Demo

This is a simple project to deploy an ML model with FastAPI. It trains a RandomForest classifier on the iris dataset and exposes a `/predict` endpoint to get predictions.

## Setup Instructions

1. **Clone the Repository:**
```
git clone https://github.com/yourusername/fastapi-ml-demo.git
cd fastapi-ml-demo
```

2. **Set Up a Dedicated Virtual Environment with Pyenv:**
If you don’t have Python 3.11 installed, you can install it via pyenv:
```
pyenv install 3.11.0
pyenv virtualenv 3.11.0 fastapi-ml-demo-env
pyenv local fastapi-ml-demo-env
```

3.	Install Dependencies:
```
pip install -r requirements.txt
```

4.	Run the Application:
```
uvicorn main:app --reload
```
Your API should now be running at http://127.0.0.1:8000.


5.	Testing the Prediction Endpoint:
You can access the automatic API documentation at http://127.0.0.1:8000/docs and test the /predict endpoint by providing values for sepal and petal measurements.


## Deployment

You can deploy this project by pushing it to a GitHub repository. From there, you can use platforms such as Heroku, Render, or Azure to deploy your FastAPI app.
