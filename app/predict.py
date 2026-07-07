from app.model_loader import model


def predict_heart(data):
    values = [[
        data.age,
        data.sex,
        data.cp,
        data.trestbps,
        data.chol,
        data.fbs,
        data.restecg,
        data.thalach,
        data.exang,
        data.oldpeak,
        data.slope,
        data.ca,
        data.thal
    ]]

    prediction = model.predict(values)[0]

    if prediction == 1:
        return {
            "prediction": 1,
            "result": "Heart Disease Detected"
        }

    return {
        "prediction": 0,
        "result": "No Heart Disease"
    }