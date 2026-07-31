import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump

# -----------------------------
# Step 1: Load Dataset
# -----------------------------
df = pd.read_csv("heart.csv")

print("First 5 Records:\n")
print(df.head())

# -----------------------------
# Step 2: Dataset Information
# -----------------------------
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# Numerical Features
numerical_features = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
print("\nNumerical Features:")
print(numerical_features)

# Target Variable
target = "target"
print("\nTarget Variable:", target)

# -----------------------------
# Step 3: Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Step 4: Split Dataset
# -----------------------------
X = df.drop(columns=[target])
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# -----------------------------
# Step 5: Train Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Step 6: Evaluate Model
# -----------------------------
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy:.4f}")

# -----------------------------
# Step 7: Save Model
# -----------------------------
dump(model, "model.pkl")

print("\nModel saved successfully as model.pkl")