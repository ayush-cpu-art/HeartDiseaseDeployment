from flask import Flask, request, jsonify, render_template
from joblib import load
import numpy as np

app = Flask(__name__)

# Load the trained model
model = load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # ---------- API (JSON) ----------
    if request.is_json:
        data = request.get_json()

        features = np.array([[
            data["age"],
            data["sex"],
            data["cp"],
            data["trestbps"],
            data["chol"],
            data["fbs"],
            data["restecg"],
            data["thalach"],
            data["exang"],
            data["oldpeak"],
            data["slope"],
            data["ca"],
            data["thal"]
        ]])

        prediction = model.predict(features)[0]

        result = (
            "Heart Disease Detected"
            if prediction == 1
            else "No Heart Disease"
        )

        return jsonify({"prediction": result})

    # ---------- HTML Form ----------
    else:
        values = [float(x) for x in request.form.values()]
        features = np.array([values])

        prediction = model.predict(features)[0]

        result = (
            "Heart Disease Detected"
            if prediction == 1
            else "No Heart Disease"
        )

        return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)