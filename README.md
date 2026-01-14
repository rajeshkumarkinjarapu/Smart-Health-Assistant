# 🩺 Smart Health Assistant
## 📌 Overview

Smart Health Assistant  is an AI-powered healthcare decision-support system that predicts the risk of Diabetes and Heart Disease, calculates BMI, and provides personalized lifestyle recommendations based on user inputs.
The application uses Machine Learning models integrated directly into a Streamlit-based interactive web interface, enabling real-time predictions without any backend server.

## 🎯 Objectives

--> Provide early health risk assessment using ML models

--> Enable instant predictions through a simple UI

--> Assist users with actionable lifestyle recommendations

--> Demonstrate an end-to-end ML deployment pipeline

## ✨ Features

🩸 Diabetes Risk Prediction

❤️ Heart Disease Prediction

⚖️ BMI Calculation & Category Classification

💡 Lifestyle Recommendation Engine

⚡ Real-time Predictions

☁️ Deployed on Streamlit Cloud

🧠 Offline-trained ML models

## 🧠 Machine Learning Models

The models were trained offline using curated healthcare datasets and later serialized using Pickle.

## Models Used:

## Diabetes Prediction

Algorithms explored: Logistic Regression, SVM, Random Forest, XGBoost

Final model selected based on performance

## Heart Disease Prediction

Supervised ML classifier

## Preprocessing

Feature scaling using StandardScaler

Feature engineering applied where required

## 🛠️ Tech Stack

Programming Language: Python

Frontend: Streamlit

Machine Learning: Scikit-learn, XGBoost

Data Handling: NumPy, Pandas

Model Serialization: Pickle

Deployment: Streamlit Cloud

## 🔍 Prerequisites

Before running the project locally, ensure you have:

Python 3.8 or above

Internet connection (for deployment)

## 📦 Dependencies

All required libraries are listed in requirements.txt:

streamlit
numpy
pandas
scikit-learn
xgboost
joblib

## ▶️ How to Run Locally
### Step 1: Clone the repository
git clone https://github.com/<your-username>/Smart-Health-Assistant.git
cd Smart-Health-Assistant

### Step 2: Install dependencies
pip install -r requirements.txt

### Step 3: Run the application
streamlit run app.py

The app will open automatically in your browser.

## ☁️ Deployment

The application is deployed using Streamlit Cloud, which directly integrates with GitHub repositories.

###Deployment Highlights:

No backend server required

Automatic dependency installation

Publicly accessible web app

## 🔗 Live Demo
https://smart-health-assistant-dwysojapltciibuxdpug5p.streamlit.app/

## 🧪 Workflow

User enters health parameters via Streamlit UI

Inputs are preprocessed and scaled

Pre-trained ML models generate predictions

Results are displayed instantly

Lifestyle recommendations are provided using rule-based logic

## 📊 Output

Diabetes Risk: High / Low

Heart Disease Risk: High / Low

BMI Value & Category

Personalized Lifestyle Tips

## 🔐 Data Privacy

No user data is stored

No external API calls

All processing happens locally within the app session

## 🚀 Future Enhancements

Doctor recommendation system

Disease probability score visualization

Integration with wearable device APIs

Multi-language support

Mobile app version

## 👨‍💻 Developer

Rajesh Kumar Kinjarapu
📍 India

📜 License

This project is developed for educational and demonstration purposes.
