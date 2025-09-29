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
- **Frontend/UI**: Streamlit
- **Visualizations**: Plotly  
- **Backend/Models**: Pretrained ML models (`.pkl` / `.pt`)  
- **Data Stream**: Simulated EEG, GSR, Eye-tracking, Facial expression signals  

---

## 📂 Project Structure
- `project/`
  - `data/`
    - `EEG.csv`
    - `GSR.csv`
    - `EYE.csv`
    - `TIVA.csv`
    - `session_logs/`
  - `models/`
    - `workload_model.pkl`
    - `accuracy_model.pkl`
    - `emotion_model.pkl`
  - `app/`
    - `dashboard.py`        — Main Streamlit/Dash application
    - `utils.py`            — Data streaming & feature extraction
    - `components.py`       — Plotting / UI helper functions
  - `README.md`

---

## ⚙️ Installation & Setup

1. **Clone the repository**
    git clone https://github.com/<your-username>/<repo-name>.git
    cd <repo-name>

2. **Create a virtual environment (recommended)**
    python -m venv venv
    source venv/bin/activate   # Linux / Mac
    venv\Scripts\activate      # Windows

3. **Install dependencies**
    pip install -r requirements.txt

4. **Run the app**
    streamlit run app/dashboard.py
   *(If using Dash, run the Dash entrypoint instead.)*

---

## 📊 Typical Workflow
1. Place pretrained models in `models/` (or point code to Drive link).  
2. Provide session CSVs in `data/session_logs/`.  
3. Start the dashboard — the app replays logs as simulated live stream.  
4. Observe real-time workload gauge, accuracy graph, and emotion transition flows.


## 🔗 Resources & Drive Link

Since the models and datasets may be large, they are stored externally.

👉 [Click here to access project files (Google Drive)](https://drive.google.com/drive/folders/1ceLALHU3k7zsFGPZ8IhNIpAbEuE6Ihah)

## 👥 Team - Group 4InLine (T1_G20)

**Faculty Mentor** : **Mrs. T.V. Deokar**
Group Members: <br>
1. Aakash Mohole <br>
2. Vinayak Vathare <br>
3. Shreyash Shetty

               


Department: CSE (Data Science)

## 📜 License

This project is developed for academic and research purposes under the IITB EdTech Internship Program.
