# # import streamlit as st
# # import pandas as pd
# # import time
# # from utils import (
# #     load_models_safe,
# #     predict_workload,
# #     predict_accuracy,
# #     predict_emotion,
# # )
# # from components import workload_gauge, accuracy_line, emotion_timeline

# # st.set_page_config(page_title="Mental State Monitoring Dashboard", layout="wide")
# # st.title("🧠 Mental State Monitoring Dashboard")

# # # ----- Load models once (cached) -----
# # models = load_models_safe(model_dir="models")
# # workload_model = models.get("workload")
# # accuracy_model = models.get("accuracy")
# # emotion_model = models.get("emotion")

# # # ---- UI: file upload and controls ----
# # st.sidebar.header("Data source")
# # uploaded_file = st.sidebar.file_uploader(
# #     "Upload CSV with model input features (rows = samples)", type=["csv"]
# # )

# # # Initialize session_state
# # if "df" not in st.session_state:
# #     st.session_state.df = None
# # if "idx" not in st.session_state:
# #     st.session_state.idx = 0
# # if "running" not in st.session_state:
# #     st.session_state.running = False
# # if "accuracy_history" not in st.session_state:
# #     st.session_state.accuracy_history = []
# # if "emotion_history" not in st.session_state:
# #     st.session_state.emotion_history = []
# # if "last_processed_index" not in st.session_state:
# #     st.session_state.last_processed_index = -1

# # # Controls
# # col1, col2, col3 = st.sidebar.columns([1, 1, 1])
# # if col1.button("⏮ Prev"):
# #     st.session_state.running = False
# #     st.session_state.idx = max(0, st.session_state.idx - 1)
# # if col2.button("▶ Start"):
# #     st.session_state.running = True
# # if col3.button("⏹ Stop"):
# #     st.session_state.running = False

# # col4, col5 = st.sidebar.columns([1, 1])
# # if col4.button("⏭ Next"):
# #     st.session_state.running = False
# #     st.session_state.idx = min(
# #         (len(st.session_state.df) - 1) if st.session_state.df is not None else 0,
# #         st.session_state.idx + 1,
# #     )
# # if col5.button("🔁 Reset"):
# #     st.session_state.running = False
# #     st.session_state.idx = 0
# #     st.session_state.accuracy_history = []
# #     st.session_state.emotion_history = []
# #     st.session_state.last_processed_index = -1

# # # Playback speed
# # speed = st.sidebar.slider(
# #     "Auto-play delay (seconds)", min_value=0.2, max_value=3.0, value=1.0, step=0.1
# # )

# # # Load CSV
# # if uploaded_file is not None:
# #     try:
# #         df = pd.read_csv(uploaded_file)
# #         if df.empty:
# #             st.sidebar.error("Uploaded CSV is empty.")
# #         else:
# #             st.session_state.df = df.reset_index(drop=True)
# #             st.sidebar.success(f"Loaded {len(st.session_state.df)} samples.")
# #             # reset if new file uploaded
# #             st.session_state.idx = 0
# #             st.session_state.accuracy_history = []
# #             st.session_state.emotion_history = []
# #             st.session_state.last_processed_index = -1
# #     except Exception as e:
# #         st.sidebar.error(f"Error reading CSV: {e}")

# # # Stop if no data
# # if st.session_state.df is None:
# #     st.info("Upload a CSV with one sample per row (features in same order as models expect).")
# #     st.stop()

# # # ---- Placeholders ----
# # workload_placeholder = st.empty()
# # accuracy_placeholder = st.empty()
# # emotion_placeholder = st.empty()

# # # Process a row
# # def process_row(row_values):
# #     try:
# #         workload = predict_workload(row_values, workload_model) if workload_model else None
# #     except Exception as e:
# #         workload = None
# #         st.error(f"Workload prediction error: {e}")

# #     try:
# #         accuracy = predict_accuracy(row_values, accuracy_model) if accuracy_model else None
# #     except Exception as e:
# #         accuracy = None
# #         st.error(f"Accuracy prediction error: {e}")

# #     try:
# #         emotion = predict_emotion(row_values, emotion_model) if emotion_model else None
# #     except Exception as e:
# #         emotion = None
# #         st.error(f"Emotion prediction error: {e}")

# #     t = len(st.session_state.accuracy_history)
# #     st.session_state.accuracy_history.append({"time": t, "accuracy": float(accuracy) if accuracy is not None else None})
# #     st.session_state.emotion_history.append({"start": t, "end": t + 1, "emotion": str(emotion) if emotion else "unknown"})

# #     return workload, accuracy, emotion

# # # ---- Main update ----
# # df = st.session_state.df
# # idx = st.session_state.idx
# # if idx >= len(df):
# #     st.session_state.running = False
# #     st.session_state.idx = len(df) - 1
# #     idx = st.session_state.idx

# # row_values = df.iloc[idx].values.astype(float)

# # if st.session_state.last_processed_index != idx:
# #     workload, accuracy, emotion = process_row(row_values)
# #     st.session_state.last_processed_index = idx
# # else:
# #     workload, accuracy, emotion = None, None, None

# # # ---- Render ----
# # with workload_placeholder.container():
# #     if workload is not None:
# #         st.plotly_chart(workload_gauge(workload), use_container_width=True)
# #     else:
# #         st.write("Workload: —")

# # with accuracy_placeholder.container():
# #     acc_df = pd.DataFrame(st.session_state.accuracy_history)
# #     st.plotly_chart(accuracy_line(acc_df), use_container_width=True)

# # with emotion_placeholder.container():
# #     emo_df = pd.DataFrame(st.session_state.emotion_history)
# #     st.plotly_chart(emotion_timeline(emo_df), use_container_width=True)

# # # Sidebar summary
# # st.sidebar.markdown("---")
# # st.sidebar.header("Latest prediction")
# # st.sidebar.write(f"Sample index: {idx}/{len(df)-1}")
# # st.sidebar.write(f"Workload: {workload}")
# # st.sidebar.write(f"Accuracy prob: {accuracy}")
# # st.sidebar.write(f"Emotion: {emotion}")

# # # Auto advance
# # if st.session_state.running:
# #     if st.session_state.idx < len(df) - 1:
# #         time.sleep(float(speed))
# #         st.session_state.idx += 1
# #         st.rerun()
# #     else:
# #         st.session_state.running = False
# #         st.success("Reached end of dataset.")

# import streamlit as st
# import pandas as pd
# import time
# import logging
# from utils import (
#     load_models_safe,
#     predict_workload,
#     predict_accuracy,
#     predict_emotion,
# )
# from components import workload_gauge, accuracy_line, emotion_timeline

# # ---------- Configure logging ----------
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     datefmt="%H:%M:%S"
# )
# logger = logging.getLogger(__name__)

# # ---------- Page Setup ----------
# st.set_page_config(page_title="Mental State Monitoring Dashboard", layout="wide")
# st.title("🧠 Mental State Monitoring Dashboard")

# # ---------- Load models (cached) ----------
# models = load_models_safe(model_dir="models")
# workload_model = models.get("workload")
# accuracy_model = models.get("accuracy")
# emotion_model = models.get("emotion")
# logger.info("Models loaded successfully.")

# # ---------- Sidebar: File upload ----------
# st.sidebar.header("Data source")
# uploaded_file = st.sidebar.file_uploader(
#     "Upload CSV with model input features (rows = samples)", type=["csv"]
# )

# # ---------- Initialize session_state ----------
# if "df" not in st.session_state:
#     st.session_state.df = None
# if "idx" not in st.session_state:
#     st.session_state.idx = 0
# if "running" not in st.session_state:
#     st.session_state.running = False
# if "accuracy_history" not in st.session_state:
#     st.session_state.accuracy_history = []
# if "emotion_history" not in st.session_state:
#     st.session_state.emotion_history = []
# if "last_processed_index" not in st.session_state:
#     st.session_state.last_processed_index = -1

# # ---------- Sidebar: Controls ----------
# col1, col2, col3 = st.sidebar.columns([1, 1, 1])
# if col1.button("⏮ Prev"):
#     st.session_state.running = False
#     st.session_state.idx = max(0, st.session_state.idx - 1)
#     logger.info(f"Moved to previous sample: index {st.session_state.idx}")

# if col2.button("▶ Start"):
#     st.session_state.running = True
#     logger.info("Streaming started.")

# if col3.button("⏹ Stop"):
#     st.session_state.running = False
#     logger.info("Streaming stopped.")

# col4, col5 = st.sidebar.columns([1, 1])
# if col4.button("⏭ Next"):
#     st.session_state.running = False
#     st.session_state.idx = min(
#         (len(st.session_state.df) - 1) if st.session_state.df is not None else 0,
#         st.session_state.idx + 1,
#     )
#     logger.info(f"Moved to next sample: index {st.session_state.idx}")

# if col5.button("🔁 Reset"):
#     st.session_state.running = False
#     st.session_state.idx = 0
#     st.session_state.accuracy_history = []
#     st.session_state.emotion_history = []
#     st.session_state.last_processed_index = -1
#     logger.info("Dashboard reset.")

# # ---------- Playback speed ----------
# speed = st.sidebar.slider(
#     "Auto-play delay (seconds)", min_value=0.2, max_value=3.0, value=1.0, step=0.1
# )

# # ---------- Load CSV ----------
# if uploaded_file is not None:
#     try:
#         df = pd.read_csv(uploaded_file)
#         if df.empty:
#             st.sidebar.error("Uploaded CSV is empty.")
#             logger.warning("Uploaded CSV was empty.")
#         else:
#             st.session_state.df = df.reset_index(drop=True)
#             st.sidebar.success(f"Loaded {len(st.session_state.df)} samples.")
#             logger.info(f"CSV loaded with {len(st.session_state.df)} samples.")
#             # Reset state
#             st.session_state.idx = 0
#             st.session_state.accuracy_history = []
#             st.session_state.emotion_history = []
#             st.session_state.last_processed_index = -1
#     except Exception as e:
#         st.sidebar.error(f"Error reading CSV: {e}")
#         logger.error(f"Error reading CSV: {e}")

# # ---------- Stop if no data ----------
# if st.session_state.df is None:
#     st.info("Upload a CSV with one sample per row (features in same order as models expect).")
#     logger.info("No CSV loaded yet. Waiting for file upload.")
#     st.stop()

# # ---------- Placeholders ----------
# workload_placeholder = st.empty()
# accuracy_placeholder = st.empty()
# emotion_placeholder = st.empty()

# # ---------- Process row ----------
# def process_row(row_values):
#     try:
#         workload = predict_workload(row_values, workload_model) if workload_model else None
#         logger.info(f"Workload prediction: {workload}")
#     except Exception as e:
#         workload = None
#         st.error(f"Workload prediction error: {e}")
#         logger.error(f"Workload prediction error: {e}")

#     try:
#         accuracy = predict_accuracy(row_values, accuracy_model) if accuracy_model else None
#         logger.info(f"Accuracy prediction: {accuracy}")
#     except Exception as e:
#         accuracy = None
#         st.error(f"Accuracy prediction error: {e}")
#         logger.error(f"Accuracy prediction error: {e}")

#     try:
#         emotion = predict_emotion(row_values, emotion_model) if emotion_model else None
#         logger.info(f"Emotion prediction: {emotion}")
#     except Exception as e:
#         emotion = None
#         st.error(f"Emotion prediction error: {e}")
#         logger.error(f"Emotion prediction error: {e}")

#     t = len(st.session_state.accuracy_history)
#     st.session_state.accuracy_history.append({"time": t, "accuracy": float(accuracy) if accuracy is not None else None})
#     st.session_state.emotion_history.append({"start": t, "end": t + 1, "emotion": str(emotion) if emotion else "unknown"})

#     return workload, accuracy, emotion

# # ---------- Main update ----------
# df = st.session_state.df
# idx = st.session_state.idx
# if idx >= len(df):
#     st.session_state.running = False
#     st.session_state.idx = len(df) - 1
#     idx = st.session_state.idx
#     logger.info("Reached last sample in CSV.")

# row_values = df.iloc[idx].values.astype(float)

# if st.session_state.last_processed_index != idx:
#     workload, accuracy, emotion = process_row(row_values)
#     st.session_state.last_processed_index = idx
#     logger.info(f"Processed row {idx}/{len(df)-1}")
# else:
#     workload, accuracy, emotion = None, None, None

# # ---------- Render ----------
# with workload_placeholder.container():
#     if workload is not None:
#         st.plotly_chart(workload_gauge(workload), use_container_width=True)
#     else:
#         st.write("Workload: —")

# with accuracy_placeholder.container():
#     acc_df = pd.DataFrame(st.session_state.accuracy_history)
#     st.plotly_chart(accuracy_line(acc_df), use_container_width=True)

# with emotion_placeholder.container():
#     emo_df = pd.DataFrame(st.session_state.emotion_history)
#     st.plotly_chart(emotion_timeline(emo_df), use_container_width=True)

# # ---------- Sidebar summary ----------
# st.sidebar.markdown("---")
# st.sidebar.header("Latest prediction")
# st.sidebar.write(f"Sample index: {idx}/{len(df)-1}")
# st.sidebar.write(f"Workload: {workload}")
# st.sidebar.write(f"Accuracy prob: {accuracy}")
# st.sidebar.write(f"Emotion: {emotion}")

# # ---------- Auto advance ----------
# if st.session_state.running:
#     if st.session_state.idx < len(df) - 1:
#         time.sleep(float(speed))
#         st.session_state.idx += 1
#         st.rerun()
#     else:
#         st.session_state.running = False
#         st.success("Reached end of dataset.")
#         logger.info("Reached end of dataset. Streaming stopped.")


import streamlit as st
import pandas as pd
import time
import logging
from utils import (
    load_models_safe,
    predict_workload,
    predict_accuracy,
    predict_emotion,
)
from components import workload_gauge, accuracy_line, emotion_timeline

# ---------- Configure logging ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

# ---------- Page Setup ----------
st.set_page_config(page_title="Mental State Monitoring Dashboard", layout="wide")
st.title("🧠 Mental State Monitoring Dashboard")

# ---------- Load models (cached) ----------
models = load_models_safe(model_dir="models")
workload_model = models.get("workload")
accuracy_model = models.get("accuracy")
emotion_model = models.get("emotion")
logger.info("✅ Models loaded successfully.")

# ---------- Sidebar: File upload ----------
st.sidebar.header("Data source")
uploaded_file = st.sidebar.file_uploader(
    "Upload CSV with model input features (rows = samples)", type=["csv"]
)

@st.cache_data
def load_csv(file):
    return pd.read_csv(file)

# ---------- Initialize session_state ----------
if "df" not in st.session_state:
    st.session_state.df = None
if "idx" not in st.session_state:
    st.session_state.idx = 0
if "running" not in st.session_state:
    st.session_state.running = False
if "accuracy_history" not in st.session_state:
    st.session_state.accuracy_history = []
if "emotion_history" not in st.session_state:
    st.session_state.emotion_history = []
if "last_processed_index" not in st.session_state:
    st.session_state.last_processed_index = -1

# ---------- Load CSV into session_state ----------
if uploaded_file is not None and st.session_state.df is None:
    try:
        df = load_csv(uploaded_file)
        if df.empty:
            st.sidebar.error("Uploaded CSV is empty.")
            logger.warning("Uploaded CSV was empty.")
        else:
            st.session_state.df = df.reset_index(drop=True)
            st.sidebar.success(f"Loaded {len(st.session_state.df)} samples.")
            logger.info(f"✅ CSV loaded with {len(st.session_state.df)} samples.")
    except Exception as e:
        st.sidebar.error(f"Error reading CSV: {e}")
        logger.error(f"❌ Error reading CSV: {e}")

# ---------- Stop if no data ----------
if st.session_state.df is None:
    st.info("Upload a CSV with one sample per row (features in same order as models expect).")
    logger.info("ℹ️ No CSV loaded yet. Waiting for file upload.")
    st.stop()

# ---------- Sidebar: Controls ----------
col1, col2, col3 = st.sidebar.columns([1, 1, 1])
if col1.button("⏮ Prev"):
    st.session_state.running = False
    st.session_state.idx = max(0, st.session_state.idx - 1)
    logger.info(f"⏮ Prev → index {st.session_state.idx}")

if col2.button("▶ Start"):
    st.session_state.running = True
    logger.info("▶ Streaming started.")

if col3.button("⏹ Stop"):
    st.session_state.running = False
    logger.info("⏹ Streaming stopped.")

col4, col5 = st.sidebar.columns([1, 1])
if col4.button("⏭ Next"):
    st.session_state.running = False
    st.session_state.idx = min(len(st.session_state.df) - 1, st.session_state.idx + 1)
    logger.info(f"⏭ Next → index {st.session_state.idx}")

if col5.button("🔁 Reset"):
    st.session_state.running = False
    st.session_state.idx = 0
    st.session_state.accuracy_history = []
    st.session_state.emotion_history = []
    st.session_state.last_processed_index = -1
    logger.info("🔁 Dashboard reset.")

# ---------- Playback speed ----------
speed = st.sidebar.slider(
    "Auto-play delay (seconds)", min_value=0.2, max_value=3.0, value=1.0, step=0.1
)

# ---------- Placeholders ----------
workload_placeholder = st.empty()
accuracy_placeholder = st.empty()
emotion_placeholder = st.empty()

# ---------- Process row ----------
def process_row(row_values):
    try:
        workload = predict_workload(row_values, workload_model) if workload_model else None
        logger.info(f"Workload prediction: {workload}")
    except Exception as e:
        workload = None
        st.error(f"Workload prediction error: {e}")
        logger.error(f"Workload prediction error: {e}")

    try:
        accuracy = predict_accuracy(row_values, accuracy_model) if accuracy_model else None
        logger.info(f"Accuracy prediction: {accuracy}")
    except Exception as e:
        accuracy = None
        st.error(f"Accuracy prediction error: {e}")
        logger.error(f"Accuracy prediction error: {e}")

    try:
        emotion = predict_emotion(row_values, emotion_model) if emotion_model else None
        logger.info(f"Emotion prediction: {emotion}")
    except Exception as e:
        emotion = None
        st.error(f"Emotion prediction error: {e}")
        logger.error(f"Emotion prediction error: {e}")

    t = len(st.session_state.accuracy_history)
    st.session_state.accuracy_history.append(
        {"time": t, "accuracy": float(accuracy) if accuracy is not None else None}
    )
    st.session_state.emotion_history.append(
        {"start": t, "end": t + 1, "emotion": str(emotion) if emotion else "unknown"}
    )

    return workload, accuracy, emotion

# ---------- Main update ----------
df = st.session_state.df
idx = st.session_state.idx
if idx >= len(df):
    st.session_state.running = False
    st.session_state.idx = len(df) - 1
    idx = st.session_state.idx
    logger.info("Reached last sample in CSV.")

row_values = df.iloc[idx].values.astype(float)

if st.session_state.last_processed_index != idx:
    workload, accuracy, emotion = process_row(row_values)
    st.session_state.last_processed_index = idx
    logger.info(f"Processed row {idx}/{len(df)-1}")
else:
    workload, accuracy, emotion = None, None, None

# ---------- Render ----------
with workload_placeholder.container():
    if workload is not None:
        st.plotly_chart(workload_gauge(workload), use_container_width=True)
    else:
        st.write("Workload: —")

with accuracy_placeholder.container():
    acc_df = pd.DataFrame(st.session_state.accuracy_history)
    st.plotly_chart(accuracy_line(acc_df), use_container_width=True)

with emotion_placeholder.container():
    emo_df = pd.DataFrame(st.session_state.emotion_history)
    st.plotly_chart(emotion_timeline(emo_df), use_container_width=True)

# ---------- Sidebar summary ----------
st.sidebar.markdown("---")
st.sidebar.header("Latest prediction")
st.sidebar.write(f"Sample index: {idx}/{len(df)-1}")
st.sidebar.write(f"Workload: {workload}")
st.sidebar.write(f"Accuracy prob: {accuracy}")
st.sidebar.write(f"Emotion: {emotion}")

# ---------- Auto advance ----------
if st.session_state.running:
    if st.session_state.idx < len(df) - 1:
        time.sleep(float(speed))
        st.session_state.idx += 1
        st.rerun()
    else:
        st.session_state.running = False
        st.success("Reached end of dataset.")
        logger.info("✅ Reached end of dataset. Streaming stopped.")
