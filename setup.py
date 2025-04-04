from setuptools import setup, find_packages

setup(
    name="fastapi-ml-demo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "scikit-learn",
        "joblib",
        "pydantic",
        "numpy",
        "python-dotenv"
    ],
)
