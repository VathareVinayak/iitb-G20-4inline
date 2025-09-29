# 🧠 Mental State Monitoring Dashboard  

## 📌 Project Overview  
This project was developed as part of the **IITB EdTech Internship 2025 (DYPCET, Track 1 - Educational Data Analysis)**.  
Our team **4InLine (Group ID: T1_G20)** worked on **Problem Statement 14: Building a Mental State Monitoring Dashboard**.  

The goal of this project is to create an **interactive real-time dashboard** that visualizes:  
- **Mental workload predictions** (Low / Medium / High)  
- **Accuracy probability** (likelihood of correct response)  
- **Emotion transitions** (e.g., Engaged → Confused → Neutral)  

This solution simulates real-time input from multimodal data sources (EEG, GSR, Eye-tracking, Facial expressions) and uses **pretrained ML models** to provide predictions.  

---

## 🚀 Features  
- 📊 **Mental Workload Panel** – Gauge chart (Low/Medium/High workload levels).  
- 📈 **Accuracy Probability Panel** – Real-time line chart with probability trends.  
- 🎭 **Emotion Transitions Panel** – Sankey diagram or timeline visualization of emotional states.  
- 👤 **Participant Summary Panel** – Snapshot of latest predictions with confidence values.  
- 🔄 **Real-time updates** – Simulated data replay at configurable refresh rates.  
- ⚡ **Scalable architecture** – Easy to extend for multi-user support, alerts, and replay mode.  

---

## 🛠️ Tech Stack  
- **Frontend/UI**: [Streamlit](https://streamlit.io/) 
- **Visualizations**: [Plotly](https://plotly.com/python/)  
- **Backend/Models**: Pretrained ML models (`.pkl` / `.pt`)  
- **Data Stream**: Simulated EEG, GSR, Eye-tracking, Facial expression signals  

---

## 📂 Project Structure  
project/
├── data/
│ ├── EEG.csv
│ ├── GSR.csv
│ ├── EYE.csv
│ ├── TIVA.csv
│ └── session_logs/
├── models/
│ ├── workload_model.pkl
│ ├── accuracy_model.pkl
│ └── emotion_model.pkl
├── app/
│ ├── dashboard.py # Main Streamlit/Dash application
│ ├── utils.py # Data stream + feature extraction
│ └── components.py # Plotting helpers
└── README.md

📊 Sample Workflow

1. Load pretrained models (workload_model.pkl, accuracy_model.pkl, emotion_model.pkl).
2. Stream simulated multimodal data (EEG, GSR, Eye, Facial expressions).
3. Generate predictions for workload, accuracy, and emotion states.
4. Update visualizations in real-time on the dashboard.

🔗 Resources & Drive Link

Since the models and datasets may be large, they are stored externally.
👉 [Click here to access project files (Google Drive)](https://drive.google.com/drive/folders/1ceLALHU3k7zsFGPZ8IhNIpAbEuE6Ihah)

👥 Team - Group 4InLine (T1_G20)

Group Members: 1. Aakash Mohole
               2. Vinayak Vathare
               3. Shreyash Shetty
               
Faculty Mentor: Mrs. T.V. Deokar

Department: CSE (Data Science)
