import sys
import json
import pandas as pd
from joblib import load

# Load model and scaler
model = load("model/model.pkl")
scaler = load("model/scaler.pkl")

# Load input data from stdin
logs = json.load(sys.stdin)
df = pd.DataFrame(logs)

# Prepare features
df["isMemoized"] = df["isMemoized"].apply(lambda val: True if val in [True, "True", "true"] else False).astype(int)
X = df[["actualDuration", "renderTime", "stateUpdates", "propsReceived", "propsUsed", "isMemoized"]]
X_scaled = scaler.transform(X)
preds = model.predict(X_scaled)

# Output suggestions
for i, row in enumerate(df["component"]):
    if preds[i] == 1:
        if df["isMemoized"].iloc[i] == 1:
            print(f"⚠️  {row}: Memoization is present, but prop bloating detected. Consider reducing unused or unstable props.")
        else:
            print(f"⚠️  {row}: Prop bloating detected. Suggest using React.memo.")
    else:
        print(f"✅ {row}: Component is already optimized.")
