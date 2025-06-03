## 📁 Folder Setup (Reference)

```
react-optimize-ai/
├── logs/
│   └── sample_logs.json       # Mock training data (20 entries)
├── model/
│   ├── train.py
│   ├── predict.py
│   ├── model.pkl              # Will be created after training
│   ├── scaler.pkl             # Saved scaler
├── cli/
│   └── reactopt.py
├── test_input.json            # Your prediction input
├── requirements.txt           # Optional (can include: scikit-learn, pandas, joblib)
```

---

## ✅ Step 1: Train the Model

### 🔹 Command:

```bash
python3 model/train.py
```

### 🔹 What it does:

- Reads `logs/sample_logs.json`
- Trains a `DecisionTreeClassifier`
- Saves `model.pkl` and `scaler.pkl` to `model/`

---

## ✅ Step 2: Create Test Input File

Example: `test_input.json`

```json
[
  {
    "component": "UserCard",
    "actualDuration": 0.6,
    "renderTime": 18.7,
    "stateUpdates": 2,
    "propsReceived": 9,
    "propsUsed": 3,
    "isMemoized": false
  }
]
```

---

## ✅ Step 3: Run Prediction via CLI

### 🔹 Command:

```bash
python3 cli/reactopt.py suggest test_input.json
```

### 🔹 Sample Output:

```
⚠️  UserCard: Prop bloating detected. Suggest using React.memo.
```

---

## 🧪 Optional: Test Another Component

Just create another JSON file like `another_component.json` and run:

python3 cli/reactopt.py suggest another_component.json

```

```

\

######################################

Perfect — you’ve given a strong starting point. Below is a full test suite of **6 JSON inputs**, each covering a **unique and realistic scenario**. This way, you can validate that your CLI tool handles all core outcomes correctly.

---

## ✅ 1. **Optimized — Not Memoized but Efficient**

```json
[
  {
    "component": "UserCard",
    "actualDuration": 0.4,
    "renderTime": 12.5,
    "stateUpdates": 0,
    "propsReceived": 9,
    "propsUsed": 8,
    "isMemoized": false
  }
]
```

> ✅ Expected Output: `Component is already optimized.`

---

## ⚠️ 2. **Bloating — Not Memoized, Few Props Used**

```json
[
  {
    "component": "UserCard",
    "actualDuration": 0.7,
    "renderTime": 22.3,
    "stateUpdates": 2,
    "propsReceived": 9,
    "propsUsed": 3,
    "isMemoized": false
  }
]
```

> ⚠️ Expected Output: `Prop bloating detected. Suggest using React.memo.`

---

## ⚠️ 3. **Bloating — Memoized but Props Are Wasted**

```json
[
  {
    "component": "UserCard",
    "actualDuration": 0.5,
    "renderTime": 19.8,
    "stateUpdates": 2,
    "propsReceived": 9,
    "propsUsed": 3,
    "isMemoized": true
  }
]
```

> ⚠️ Expected Output: `Memoization is present, but prop bloating detected.`

---

## ✅ 4. **Optimized — Memoized, High Prop Usage, Low Renders**

```json
[
  {
    "component": "UserCard",
    "actualDuration": 0.3,
    "renderTime": 11.2,
    "stateUpdates": 0,
    "propsReceived": 9,
    "propsUsed": 9,
    "isMemoized": true
  }
]
```

> ✅ Expected Output: `Component is already optimized.`

---

## ⚠️ 5. **Borderline — Memoized, Good Usage but Still High Re-renders**

```json
[
  {
    "component": "UserCard",
    "actualDuration": 1.2,
    "renderTime": 29.7,
    "stateUpdates": 3,
    "propsReceived": 9,
    "propsUsed": 7,
    "isMemoized": true
  }
]
```

> ⚠️ Expected Output: `Memoization is present, but prop bloating detected.`

---

## ⚠️ 6. **Non-Memoized, High Props Used, Minor State Updates**

```json
[
  {
    "component": "UserCard",
    "actualDuration": 0.6,
    "renderTime": 17.4,
    "stateUpdates": 1,
    "propsReceived": 9,
    "propsUsed": 8,
    "isMemoized": false
  }
]
```

              <UserCardDes
                key={user.id}
                id={user.id}
                name={user.name}
                email={user.email}
                role={user.role}
              />
