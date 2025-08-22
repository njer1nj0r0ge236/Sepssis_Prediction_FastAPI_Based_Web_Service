from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("sepssis_model.pkl")

# Initialize FastAPI app
app = FastAPI(title="Sepssis Prediction API", version="1.0")

# Define input data model with exact features
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
    # Convert incoming data to DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # Ensure the columns match the trained model's features
    input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)
    
    # Make prediction
    prediction = model.predict(input_df)[0]
    
    # Convert prediction to human-readable form
    result = "Positive" if prediction == 1 else "Negative"
    
    return {"Sepssis_Prediction": result}
