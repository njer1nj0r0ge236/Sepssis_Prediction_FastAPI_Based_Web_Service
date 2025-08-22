# 🩺 Sepsis Prediction API

# 📝 Project Scenario  
Sepsis is a life-threatening condition caused by the body’s response to infection. Early detection is critical for improving patient survival rates. With machine learning classification models, healthcare providers can predict the likelihood of sepsis and take timely action.  

This project is a **Machine Learning API** for predicting **Sepsis** in patients based on medical records.  
The model was trained on patient datasets from Kaggle and deployed using **FastAPI**.

## 📂 Dataset
The dataset comes from Kaggle:  
👉 [Sepsis Patients Dataset](https://www.kaggle.com/datasets/chaunguynnghunh/sepsis/data)

Files used:
- `Paitients_Files_Train (1).csv` → Training data- 599 records 
- `Paitients_Files_Test (1).csv` → Test data- 169 records 

📌 Note: Datasets were uploaded into Google Colab for preprocessing, model training, and evaluation.  


The train_df(Training data) was split into:
- **Training Dataset (80%)** – used to build and train the machine learning model.  
- **Validation Dataset (20%)** – used to evaluate model performance.

The test_df(Test data)
- **Testing Dataset** – used for final model predictions.  
---

## 🚀 Project Objectives  
- Build an end-to-end ML pipeline for sepsis prediction.  
- Perform data preprocessing (handle missing values, encode categorical variables).  
- Train and evaluate multiple ML models: Logistic Regression, Random Forest, XGBoost.  
- Optimize models with hyperparameter tuning (focus on recall for positive class).  
- Deploy the best-performing model as a RESTful API using FastAPI.  

---

## 🛠️ Tools & Technologies  
- **Python**: Pandas, NumPy, Scikit-learn, XGBoost  
- **Google Colab**: for model building & experimentation  
- **FastAPI**: for serving the trained model as a REST API  
- **Uvicorn**: ASGI server to run the API  
- **Docker**: containerization and deployment  
- **GitHub**: version control & collaboration  

---

## ⚙️ How It Works  
1. **Data Preprocessing**  
   - Handle missing values, encode categorical features, normalize numerical features.  
   - Final features used: `PRG, PL, PR, SK, TS, M11, BD2, Age, Insurance`.
   - Target variable: `Sepssis`

2. **Model Training**  
   - Logistic Regression (baseline).  
   - Random Forest & XGBoost (with hyperparameter tuning).  
   - Logistic Regression achieved the best recall and was selected.

3. **Model Evaluation**  
   - Metrics: Accuracy, Precision, Recall, F1-score.

   **Logistic Regression** - Recall (positive class): 0.643 
   **Logistic Regression** won after **hyperparameters tuning**
   - Emphasis on **recall for positive cases (sepsis detection)**.  

4. **API Development**  
   - FastAPI provides endpoints:  
   - `GET /` → Welcome message  
   - `POST /predict` → Returns sepsis prediction based on input features.  

5. **Dockerization**  
   - Dockerfile builds and runs the FastAPI app in a lightweight container.  

---

## 📝 Note  
- Model training work is saved in Google Colab (`Sepsis_Prediction.ipynb`).  
- Final trained model is stored as `sepssis_model.pkl`.  

---

## 🚀 API Features  
- **🏠 Home Endpoint** – Welcome message.  
- **🤖 Predict Endpoint** – Accepts patient input (JSON) and outputs:  
  ```json
  {
    "Sepssis_Prediction": "Positive"
  }

## 🚀 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/sepsis-api.git
cd sepsis-api

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Running the API locally
# Start the FastAPI server:
uvicorn main:app --reload

# Open your browser and test:
http://127.0.0.1:8000/docs  
```
## ✨ Future Improvements
- Containerize the application with Docker for portability 
- Add more features for patient monitoring
- Deploy to cloud (AWS/GCP/Heroku)
- Create a frontend dashboard

## 🌍 Deployment
The project will soon be deployed on Docker:
👉 [Live App]

## 👩‍💻 Author  
Developed by [Marydiana Njoroge](https://marydiananjorogeportfolio.vercel.app/)  
💼 [LinkedIn](https://www.linkedin.com/in/marydiana-njoroge-41b236244/) 
🐙 [GitHub](https://github.com/njer1nj0r0ge236)  
✍️ [Medium](https://medium.com/@njorogediana236)  


## 📌 License
This project is licensed under the [MIT License](./LICENSE) – see the LICENSE file for details.

