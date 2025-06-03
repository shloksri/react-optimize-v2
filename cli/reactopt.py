import argparse
import json
import pandas as pd
from joblib import load
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "scripts"))
from analyze_component import analyze_component

# Load model and scaler
model = load("model/model.pkl")
scaler = load("model/scaler.pkl")

def suggest_optimization(data):
    df = pd.DataFrame(data)
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

    suggest_parser = subparsers.add_parser("suggest", help="Suggest optimization for a component or JSON file")
    suggest_parser.add_argument("input", type=str, help="Path to input .json or .jsx file")

    args = parser.parse_args()

    if args.command == "suggest":
        if args.input.endswith(".json"):
            with open(args.input) as f:
                logs = json.load(f)
        elif args.input.endswith(".jsx"):
            logs = analyze_component(args.input)
        else:
            print("Unsupported file type. Provide either .json or .jsx")
            sys.exit(1)

        suggest_optimization(logs)
    else:
        parser.print_help()
