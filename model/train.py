# model/train.py

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from joblib import dump
import json

# Load mock training data
with open('./logs/sample_logs.json') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Features and label
X = df[["actualDuration", "renderTime", "stateUpdates", "propsReceived", "propsUsed", "isMemoized"]]

# Ensure isMemoized is boolean then cast to int
X = X.copy()
X["isMemoized"] = X["isMemoized"].apply(lambda val: True if val in [True, "True", "true"] else False).astype(int)

y = df["label"]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save model and scaler
dump(model, "model/model.pkl")
dump(scaler, "model/scaler.pkl")

print("✅ Model trained and saved as model.pkl")
