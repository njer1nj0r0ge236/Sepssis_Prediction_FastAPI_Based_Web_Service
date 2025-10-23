from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import gradio as gr

# Load the trained model
model = joblib.load("sepssis_model.pkl")

# Initialize FastAPI app
app = FastAPI(title="Sepssis Prediction API", version="1.0")

# Define input data model
class PatientData(BaseModel):
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance: int

@app.get("/")
def home():
    return {"message": "Welcome to the Sepssis Prediction API"}

@app.post("/predict")
def predict(data: PatientData):
    input_df = pd.DataFrame([data.dict()])
    input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)
    prediction = model.predict(input_df)[0]
    result = "Positive" if prediction == 1 else "Negative"
    return {"Sepssis_Prediction": result}

# -------------------------------
# Gradio Interface for Web UI
# -------------------------------
def predict_ui(PRG, PL, PR, SK, TS, M11, BD2, Age, Insurance):
    input_df = pd.DataFrame([{
        "PRG": PRG,
        "PL": PL,
        "PR": PR,
        "SK": SK,
        "TS": TS,
        "M11": M11,
        "BD2": BD2,
        "Age": Age,
        "Insurance": Insurance
    }])
    input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)
    prediction = model.predict(input_df)[0]
    return "🩺 Sepsis Prediction: Positive ✅" if prediction == 1 else "🩺 Sepsis Prediction: Negative ❌"

demo = gr.Interface(
    fn=predict_ui,
    inputs=[
        gr.Number(label="PRG"),
        gr.Number(label="PL"),
        gr.Number(label="PR"),
        gr.Number(label="SK"),
        gr.Number(label="TS"),
        gr.Number(label="M11"),
        gr.Number(label="BD2"),
        gr.Number(label="Age"),
        gr.Number(label="Insurance")
    ],
    outputs="text",
    title="🩺 Sepssis Prediction App",
    description="Enter patient details to predict Sepsis likelihood using a trained ML model."
)

demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
