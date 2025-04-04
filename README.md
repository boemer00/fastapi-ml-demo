# FastAPI ML Demo

This is a simple project to deploy an ML model with FastAPI. It trains a RandomForest classifier on the iris dataset and exposes a `/predict` endpoint to get predictions.

## Setup Instructions

1. **Clone the Repository:**
```
git clone https://github.com/yourusername/fastapi-ml-demo.git
cd fastapi-ml-demo
```

2. **Set Up a Dedicated Virtual Environment with Pyenv:**
If you don't have Python 3.11 installed, you can install it via pyenv:
```
pyenv install 3.11.0
pyenv virtualenv 3.11.0 fastapi-ml-demo-env
pyenv local fastapi-ml-demo-env
```

3.	**Install Dependencies:**
```
pip install -r requirements.txt
```

4.	**Run the Application:**
```
uvicorn main:app --reload
```
Your API should now be running at http://127.0.0.1:8000.


5.	**Testing the Prediction Endpoint:**
You can access the automatic API documentation at http://127.0.0.1:8000/docs and test the /predict endpoint by providing values for sepal and petal measurements.


## Deployment

### Vercel Deployment

This project is configured for deployment on Vercel through GitHub Actions CI/CD pipeline.

1. **Prerequisites:**
   - A Vercel account
   - A GitHub repository for this project

2. **Setup GitHub Secrets:**
   To enable automated deployments, add the following secrets to your GitHub repository:
   - `VERCEL_TOKEN`: Your Vercel API token
   - `VERCEL_ORG_ID`: Your Vercel organization ID
   - `VERCEL_PROJECT_ID`: Your Vercel project ID

3. **CI/CD Pipeline:**
   The project includes a GitHub Actions workflow that:
   - Runs tests on push to master branch or pull requests
   - Automatically deploys to Vercel when tests pass on the master branch

### Manual Deployment

You can also deploy this project manually to platforms such as Heroku, Render, or Azure.
