# ❤️ Heart Disease Prediction System

An end-to-end Machine Learning project that predicts whether a patient is at risk of heart disease based on clinical parameters. The application is built using **Python**, **Scikit-learn**, and **Flask**, deployed on **Render**, and managed using **GitHub**.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. This project uses a Machine Learning classification model to predict the likelihood of heart disease from patient health information.

The application allows users to enter patient details through a web interface or send data as JSON to a REST API and instantly receive a prediction.

---

## 🚀 Features

- Data preprocessing using Pandas
- Random Forest Classification Model
- Model serialization using Joblib
- Flask REST API
- User-friendly web interface
- JSON API support
- GitHub version control
- Cloud deployment using Render

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML
- CSS
- Git
- GitHub
- Render

---

## 📂 Project Structure

```
HeartDiseaseDeployment/
│
├── app.py
├── train_model.py
├── model.pkl
├── heart.csv
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
```

---

## 📊 Dataset

**Heart Disease Prediction Dataset**

The dataset contains patient medical information such as:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Rest ECG
- Maximum Heart Rate
- Exercise Induced Angina
- Old Peak
- Slope
- Number of Major Vessels
- Thalassemia

Target:

- **0 → No Heart Disease**
- **1 → Heart Disease**

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/HeartDiseaseDeployment.git
```

Move into the project folder

```bash
cd HeartDiseaseDeployment
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the model training

```bash
python train_model.py
```

Start the Flask application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 🌐 API Endpoint

### POST

```
/predict
```

Example JSON

```json
{
  "age":63,
  "sex":1,
  "cp":3,
  "trestbps":145,
  "chol":233,
  "fbs":1,
  "restecg":0,
  "thalach":150,
  "exang":0,
  "oldpeak":2.3,
  "slope":0,
  "ca":0,
  "thal":1
}
```

Example Response

```json
{
    "prediction":"Heart Disease Detected"
}
```

---

## 📈 Model

Algorithm Used:

- Random Forest Classifier

Evaluation Metric:

- Accuracy Score

The trained model is saved as:

```
model.pkl
```

---

## 📸 Screenshots

### Home Page

_Add screenshot here_

### Prediction Result

_Add screenshot here_

---

## 🔗 Live Demo

Render Deployment

```
https://your-render-link.onrender.com
```

---

## 💻 GitHub Repository

```
https://github.com/your-username/HeartDiseaseDeployment
```

---

## 📝 Conclusion

This project demonstrates a complete end-to-end machine learning workflow, from data preprocessing and model training to deployment as a Flask web application. The Random Forest classifier provides reliable predictions for heart disease risk, while GitHub and Render simplify version control and cloud deployment. The project also introduces fundamental MLOps concepts such as model serialization, API development, and production deployment.

---

## 👨‍💻 Author

**Ayush**

B.Tech AI & ML