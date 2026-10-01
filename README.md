#  Heart Disease Prediction System

An end-to-end Machine Learning web application that predicts whether a patient is at risk of heart disease using clinical parameters. The project is built with **Python**, **Scikit-learn**, and **Flask**, version-controlled with **GitHub**, and deployed on **Render**.

---

##  Project Overview

Heart disease is one of the leading causes of death worldwide. This application uses a trained **Random Forest Classifier** to predict the likelihood of heart disease based on patient health data.

Users can either:
- Enter patient details through a simple web interface.
- Send JSON data to the REST API and receive predictions instantly.

---

##  Features

- Heart Disease Prediction using Machine Learning
- Data preprocessing with Pandas
- Random Forest Classification Model
- Model serialization using Joblib
- Flask REST API
- Responsive and user-friendly interface
- Cloud deployment using Render
- Version control using GitHub

---

##  Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML5
- CSS3
- Git
- GitHub
- Render

---

##  Project Structure

```text
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

##  Dataset

The project uses the **Heart Disease Prediction Dataset** containing patient clinical information such as:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Rest ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Old Peak
- Slope
- Number of Major Vessels (CA)
- Thalassemia

**Target Variable**

- `0` → No Heart Disease
- `1` → Heart Disease

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ayush-cpu-art/HeartDiseaseDeployment.git
```

Move into the project directory:

```bash
cd HeartDiseaseDeployment
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train_model.py
```

Run the Flask application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

##  API Endpoint

### POST `/predict`

Example JSON Input

```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```

Example Response

```json
{
  "prediction": "Heart Disease Detected"
}
```

---

##  Machine Learning Model

**Algorithm Used**

- Random Forest Classifier

**Evaluation Metric**

- Accuracy Score

The trained model is stored as:

```
model.pkl
```

---

##  Live Demo

**Render Deployment**

https://heartdiseasedeployment-3g72.onrender.com

---

##  GitHub Repository

https://github.com/ayush-cpu-art/HeartDiseaseDeployment

---



##  Conclusion

This project demonstrates the complete machine learning deployment workflow, including data preprocessing, model training, serialization, API development, version control, and cloud deployment. The Random Forest classifier provides reliable predictions, while Flask and Render enable the model to be served as a live web application. The project also introduces essential MLOps concepts such as model packaging, deployment, and serving predictions through a REST API.

---

## 👨‍💻 Author

**Ayush**

B.Tech – Artificial Intelligence & Machine Learning
