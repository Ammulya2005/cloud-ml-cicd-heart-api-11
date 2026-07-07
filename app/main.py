from fastapi import FastAPI

from app.schemas import HeartData
from app.predict import predict_heart

app = FastAPI(
    title="Heart Disease Prediction API",
    version="1.0.0",
    description="Cloud CI/CD ML Deployment Assignment"
)


@app.get("/")
def home():
    return {
        "message": "Heart Disease Prediction API is Running"
    }


@app.post("/predict")
def predict(data: HeartData):
    return predict_heart(data)