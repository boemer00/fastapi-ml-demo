import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

def train_model(model_file: str):
    # Load iris data and train a RandomForest classifier
    iris = load_iris()
    X, y = iris.data, iris.target
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, model_file)
    print(f"Model trained and saved to {model_file}")

def predict_iris(input_data, model_file: str):
    # Load the trained model and predict
    model = joblib.load(model_file)
    prediction = model.predict(input_data)
    iris = load_iris()
    target_names = iris.target_names
    return target_names[prediction[0]]
