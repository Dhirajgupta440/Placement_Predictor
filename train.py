import pandas as pd, joblib, sys
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

DATA_PATH  = sys.argv[1] if len(sys.argv) > 1 else "placement.csv"
MODEL_PATH = "modelpp.pkl"
FEATURES   = ["cgpa", "iq"]
TARGET     = "placement"

df = pd.read_csv(DATA_PATH)
X, y = df[FEATURES], df[TARGET]

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("lr",     LogisticRegression(max_iter=1000))
])
pipeline.fit(X, y)
joblib.dump(pipeline, MODEL_PATH)
print(f"Model saved to {MODEL_PATH} – accuracy: {pipeline.score(X, y):.3f}")