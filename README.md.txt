 🩺 Heart Disease Risk Prediction App

An end-to-end Machine Learning web application built with **Python**, **Scikit-Learn**, and **Streamlit** to estimate a patient's risk of heart disease based on clinical diagnostic features.

---

📌 Project Overview
Heart disease is one of the leading causes of death worldwide. Early detection and risk assessment can significantly improve clinical outcomes. 

In medical diagnostic models, minimizing **False Negatives** (failing to identify an at-risk patient) is much more critical than minimizing False Positives. This project trains and evaluates multiple classification algorithms, optimizes for high **Recall**, and deploys the final model into an intuitive, user-friendly interactive web interface.

---

 🚀 Live Demo
- **Web App**: https://clinical-heart-disease-risk-prediction-uxjtuk3dlkxohzzq8a3dlh.streamlit.app/
- **GitHub Repository**: https://github.com/lokeshkovvuri007/Clinical-heart-disease-risk-prediction
---

 🛠️ Tech Stack & Libraries
- **Language**: Python 3.10+
- **Machine Learning**: Scikit-Learn
- **Data Manipulation & Analysis**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Model Deployment**: Streamlit, Joblib

---

📊 Dataset & Features
The model is trained on clinical patient diagnostic records with 13 key parameters:

| Feature | Description |
| :--- | :--- |
| `age` | Patient age in years |
| `sex` | Biological sex (1 = Male, 0 = Female) |
| `cp` | Chest pain type (Values 0–3) |
| `trestbps` | Resting blood pressure (in mm Hg upon admission) |
| `chol` | Serum cholesterol level (in mg/dl) |
| `fbs` | Fasting blood sugar > 120 mg/dl (1 = True, 0 = False) |
| `restecg` | Resting electrocardiographic results (Values 0–2) |
| `thalach` | Maximum heart rate achieved during exercise |
| `exang` | Exercise-induced angina (1 = Yes, 0 = No) |
| `oldpeak` | ST depression induced by exercise relative to rest |
| `slope` | Slope of the peak exercise ST segment (Values 0–2) |
| `ca` | Number of major vessels (0–4) colored by fluoroscopy |
| `thal` | Thalassemia (1 = Normal, 2 = Fixed defect, 3 = Reversible defect) |
| **`target`** | **Diagnosis (0 = Healthy / Low Risk, 1 = Heart Disease / High Risk)** |

---

 🔬 Model Development & Performance
Multiple classification models were benchmarked and evaluated using Stratified train-test splits and feature scaling:
- **Logistic Regression**: Baseline linear probabilistic classifier.
- **K-Nearest Neighbors (KNN)**: Tuned via 5-fold `GridSearchCV`.
- **Gaussian Naive Bayes**: Probabilistic baseline for independent features.
- **Random Forest Classifier**: Ensemble of 100 decision trees (Selected final model for production).

 Final Model Metrics (Test Set):
- **Accuracy**: ~83.6%
- **Recall (Sensitivity)**: **~97.0%** *(High sensitivity to reduce missed diagnoses)*
- **Precision**: ~78.0%
- **F1-Score**: ~86.5%

---

 💻 How to Run Locally

 1. Clone the repository
```bash
git clone https://github.com/lokeshkovvuri007/Clinical-heart-disease-risk-prediction

2.Create a virtual environment:

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


3.Install dependencies:
pip install -r requirements.txt


4. Train the model and generate serialized artifacts:

python train_model.py
(This generates heart_disease_model.pkl and scaler.pkl in your project folder.)


5. Launch the Streamlit web application:
streamlit run app.py

⚠️ Disclaimer
This application is built solely for educational and research demonstration purposes. It should not be used as a substitute for professional medical advice, diagnosis, or clinical decision-making.


📁 Repository Structure:

├── heart.csv                     # Clinical dataset
├── train_model.py                # Pipeline script to train & serialize model
├── app.py                        # Streamlit web application interface
├── heart_disease_model.pkl       # Trained Random Forest model
├── scaler.pkl                    # StandardScaler fitted on training features
├── requirements.txt              # Project package dependencies
└── README.md                     # Project documentation


👤 Author
Kovvuri Lokesh Reddy

LinkedIn: www.linkedin.com/in/lokesh-reddy-kovvuri-83280k


GitHub: lokeshkovvuri007










