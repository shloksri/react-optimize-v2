import argparse
import json
import pandas as pd
from joblib import load

# Load model and scaler
model = load("model/model.pkl")
scaler = load("model/scaler.pkl")

def suggest_optimization(input_path):
    with open(input_path) as f:
        logs = json.load(f)

    df = pd.DataFrame(logs)
    df["isMemoized"] = df["isMemoized"].apply(lambda val: True if val in [True, "True", "true"] else False).astype(int)

    X = df[["actualDuration", "renderTime", "stateUpdates", "propsReceived", "propsUsed", "isMemoized"]]
    X_scaled = scaler.transform(X)

    preds = model.predict(X_scaled)

    for i, row in enumerate(df["component"]):
        if preds[i] == 1:
            if df["isMemoized"].iloc[i] == 1:
                print(f"⚠️  {row}: Memoization is present, but prop bloating detected. Consider reducing unused or unstable props.")
            else:
                print(f"⚠️  {row}: Prop bloating detected. Suggest using React.memo.")
        else:
            print(f"✅ {row}: Component is already optimized.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI React Optimization CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    suggest_parser = subparsers.add_parser("suggest", help="Suggest optimization for a component")
    suggest_parser.add_argument("input", type=str, help="Path to input JSON file")

    args = parser.parse_args()

    if args.command == "suggest":
        suggest_optimization(args.input)
    else:
        parser.print_help()
