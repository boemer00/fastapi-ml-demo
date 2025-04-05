# FastAPI ML Demo with Streamlit

This project demonstrates a machine learning model deployment with both a FastAPI backend API and a Streamlit interactive frontend. It classifies iris flowers into species based on their measurements using a simple rule-based model.

## Demo

You can access the live Streamlit app here: [Iris Classifier App](https://your-streamlit-url-here)

## Architecture

This project has two main components:
1. **FastAPI Backend API**: For programmatic access to the iris classification model
2. **Streamlit Frontend**: For interactive exploration and visualization

## Features

- 🌸 Classification of iris flowers (setosa, versicolor, virginica) based on measurements
- 🚀 Fast, type-checked API using FastAPI
- 📊 Interactive UI with Streamlit
- 🧪 Comprehensive test suite
- 🔄 CI/CD pipeline with GitHub Actions

## Setup Instructions

### 1. Clone the Repository:
```bash
git clone https://github.com/yourusername/fastapi-ml-demo.git
cd fastapi-ml-demo
```

### 2. Set Up a Dedicated Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Application:
```bash
uvicorn app.api:app --reload
```
The API will be available at http://127.0.0.1:8000.

### 5. Run the Streamlit Application:
```bash
streamlit run streamlit_app.py
```
The Streamlit app will open automatically in your browser.

## API Documentation

When running the FastAPI app locally, you can access the automatic API documentation at http://127.0.0.1:8000/docs.

### Endpoints

#### GET /
Returns a welcome message to confirm the API is running.

#### POST /predict
Predicts the iris species based on flower measurements.

**Request Body**:
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

**Response**:
```json
{
  "prediction": "setosa"
}
```

## Model Information

The project uses a simple rule-based model for iris classification:
- If petal length < 2.5 cm → **setosa**
- If petal length between 2.5 and 4.9 cm → **versicolor**
- If petal length > 4.9 cm → **virginica**

This rule-based approach achieves approximately 96% accuracy on the iris dataset while keeping the implementation simple and deployment-friendly.

## Testing

Run tests with:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=./ --cov-report=xml
```

## Deployment

### Streamlit Cloud Deployment

This project is configured for deployment on Streamlit Cloud:

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub repository
4. Select `streamlit_app.py` as the main file
5. Deploy!

### FastAPI Deployment Options

The FastAPI backend can be deployed to various platforms:

- **Render**: Good free tier option with Python support
- **Fly.io**: Provides global deployment with a generous free tier
- **Railway**: Simple deployment process with GitHub integration
- **PythonAnywhere**: Specifically designed for Python applications

## Development Workflow

1. Make changes to the code
2. Run tests locally to ensure everything works
3. Push changes to GitHub
4. GitHub Actions automatically runs the test suite
5. Streamlit Cloud automatically redeploys the application

## Key Technologies

- **FastAPI**: Modern, high-performance web framework
- **Pydantic**: Data validation using Python type annotations
- **Streamlit**: Interactive data app framework
- **pytest**: Testing framework
- **GitHub Actions**: CI/CD automation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
