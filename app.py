"""
Placement Predictor – Gradio app for Hugging Face Spaces
-------------------------------------------------------
• On first run, trains a Logistic Regression model from placement.csv
• Saves model to modelpp.pkl for future fast reloads
• Exposes a neat Gradio interface with 2 numeric sliders
"""

import os, joblib, pandas as pd, numpy as np, gradio as gr
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

MODEL_PATH  = "modelpp.pkl"
DATA_PATH   = "placement.csv"
FEATURES    = ["cgpa", "iq"]
TARGET      = "placement"

def train_model() -> Pipeline:
    """Train a simple Logistic Regression model and persist it."""
    if not os.path.exists(DATA_PATH):
        # Create a tiny synthetic dataset if author forgot to commit CSV
        rng = np.random.default_rng(42)
        X = rng.uniform([5, 90], [10, 150], size=(200, 2))  # 2 features now
        y = (0.5 * X[:, 0] + 0.02 * X[:, 1] > 6).astype(int)  # adjust decision rule
        df = pd.DataFrame(X, columns=FEATURES)
        df[TARGET] = y
    else:
        df = pd.read_csv(DATA_PATH)

    X, y = df[FEATURES], df[TARGET]
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    pipe.fit(X, y)
    joblib.dump(pipe, MODEL_PATH)
    return pipe

# ------------------------------------------------------------------
# Load or train the model
# ------------------------------------------------------------------
if os.path.exists(MODEL_PATH):
    model: Pipeline = joblib.load(MODEL_PATH)
else:
    model: Pipeline = train_model()

# ------------------------------------------------------------------
# Inference function (2 features only)
# ------------------------------------------------------------------
def predict_placement(cgpa, iq):
    """Return 'Placed' or 'Not Placed'."""
    feats = [[cgpa, iq]]
    proba = model.predict_proba(feats)[0, 1]
    pred  = "🎉 Placed" if proba >= 0.5 else "❌ Not Placed"
    return f"{pred}  (probability = {proba:.2%})"

# ------------------------------------------------------------------
# Build Gradio UI (2 sliders)
# ------------------------------------------------------------------
demo = gr.Interface(
    fn=predict_placement,
    inputs=[
        gr.Slider(5.0, 10.0, step=0.1, label="CGPA (0-10)"),
        gr.Slider(90, 150, step=1,     label="IQ Score"),
    ],
    outputs=gr.Text(label="Prediction"),
    title="Campus Placement Predictor",
    description=(
        "A demo Logistic Regression model.\n"
        "  •  Enter a candidate’s stats.\n"
        "  •  Click **Submit** to see placement likelihood.\n\n"
        "Replace **placement.csv** with your real training data "
        "and retrain to improve accuracy."
    ),
    allow_flagging="never",
)

if __name__ == "__main__":
    demo.launch()