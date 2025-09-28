# # utils.py
# import joblib
# import numpy as np
# import os
# import warnings
# import streamlit as st

# # Suppress sklearn warnings for clean logs
# warnings.filterwarnings("ignore", category=UserWarning)
# warnings.filterwarnings("ignore", category=FutureWarning)

# @st.cache_resource
# def load_models_safe(model_dir: str = "models"):
#     mapping = {
#         "workload": ["rf_workload.pkl", "workload_model.pkl"],
#         "accuracy": ["rf_accuracy.pkl", "accuracy_model.pkl"],
#         "emotion": ["rf_emotion.pkl", "emotion_model.pkl"],
#     }
#     loaded = {"workload": None, "accuracy": None, "emotion": None}
#     for key, candidates in mapping.items():
#         for fname in candidates:
#             path = os.path.join(model_dir, fname)
#             if os.path.exists(path):
#                 try:
#                     loaded[key] = joblib.load(path)
#                     print(f"Loaded {key} model from {path}")
#                     break
#                 except Exception as e:
#                     print(f"Failed to load {path}: {e}")
#     return loaded

# def _ensure_array(features):
#     arr = np.array(features, dtype=float)
#     return arr.flatten()

# def predict_workload(features, workload_model):
#     feats = _ensure_array(features)
#     if workload_model is None:
#         raise RuntimeError("Workload model not loaded.")
#     expected = getattr(workload_model, "n_features_in_", len(feats))
#     if len(feats) > expected:
#         feats = feats[:expected]
#     elif len(feats) < expected:
#         feats = np.pad(feats, (0, expected - len(feats)))
#     pred = workload_model.predict([feats])[0]
#     try:
#         return float(pred)
#     except Exception:
#         mapping = {"low": 0.0, "med": 1.0, "medium": 1.0, "high": 2.0}
#         return mapping.get(str(pred).lower(), 0.0)

# def predict_accuracy(features, accuracy_model):
#     feats = _ensure_array(features)
#     if accuracy_model is None:
#         raise RuntimeError("Accuracy model not loaded.")
#     expected = getattr(accuracy_model, "n_features_in_", len(feats))
#     if len(feats) > expected:
#         feats = feats[:expected]
#     elif len(feats) < expected:
#         feats = np.pad(feats, (0, expected - len(feats)))
#     if hasattr(accuracy_model, "predict_proba"):
#         probas = accuracy_model.predict_proba([feats])[0]
#         if 1 in accuracy_model.classes_:
#             idx = list(accuracy_model.classes_).index(1)
#             return float(probas[idx])
#         return float(probas[-1])
#     else:
#         pred = accuracy_model.predict([feats])[0]
#         return 1.0 if str(pred) in ("1", "true", "yes") else 0.0

# def predict_emotion(features, emotion_model):
#     feats = _ensure_array(features)
#     if emotion_model is None:
#         raise RuntimeError("Emotion model not loaded.")
#     expected = getattr(emotion_model, "n_features_in_", len(feats))
#     if len(feats) > expected:
#         feats = feats[:expected]
#     elif len(feats) < expected:
#         feats = np.pad(feats, (0, expected - len(feats)))
#     return emotion_model.predict([feats])[0]


import joblib
import numpy as np
import os
import streamlit as st
import warnings

# Suppress sklearn warnings for cleaner logs
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

@st.cache_resource
def load_models_safe(model_dir: str = "models"):
    mapping = {
        "workload": ["rf_workload.pkl", "workload_model.pkl"],
        "accuracy": ["rf_accuracy.pkl", "accuracy_model.pkl"],
        "emotion": ["rf_emotion.pkl", "emotion_model.pkl"],
    }
    loaded = {"workload": None, "accuracy": None, "emotion": None}
    for key, candidates in mapping.items():
        for fname in candidates:
            path = os.path.join(model_dir, fname)
            if os.path.exists(path):
                try:
                    loaded[key] = joblib.load(path)
                    break
                except Exception as e:
                    print(f"❌ Failed to load {path}: {e}")
    return loaded

def _ensure_array(features):
    arr = np.array(features, dtype=float)
    return arr.flatten()

def predict_workload(features, workload_model):
    feats = _ensure_array(features)
    if workload_model is None:
        raise RuntimeError("Workload model not loaded.")
    expected = getattr(workload_model, "n_features_in_", len(feats))
    if len(feats) > expected:
        feats = feats[:expected]
    elif len(feats) < expected:
        feats = np.pad(feats, (0, expected - len(feats)))
    pred = workload_model.predict([feats])[0]
    try:
        return float(pred)
    except Exception:
        mapping = {"low": 0.0, "med": 1.0, "medium": 1.0, "high": 2.0}
        return mapping.get(str(pred).lower(), 0.0)

def predict_accuracy(features, accuracy_model):
    feats = _ensure_array(features)
    if accuracy_model is None:
        raise RuntimeError("Accuracy model not loaded.")
    expected = getattr(accuracy_model, "n_features_in_", len(feats))
    if len(feats) > expected:
        feats = feats[:expected]
    elif len(feats) < expected:
        feats = np.pad(feats, (0, expected - len(feats)))
    if hasattr(accuracy_model, "predict_proba"):
        probas = accuracy_model.predict_proba([feats])[0]
        if 1 in accuracy_model.classes_:
            idx = list(accuracy_model.classes_).index(1)
            return float(probas[idx])
        return float(probas[-1])
    else:
        pred = accuracy_model.predict([feats])[0]
        return 1.0 if str(pred) in ("1", "true", "yes") else 0.0

def predict_emotion(features, emotion_model):
    feats = _ensure_array(features)
    if emotion_model is None:
        raise RuntimeError("Emotion model not loaded.")
    expected = getattr(emotion_model, "n_features_in_", len(feats))
    if len(feats) > expected:
        feats = feats[:expected]
    elif len(feats) < expected:
        feats = np.pad(feats, (0, expected - len(feats)))
    return emotion_model.predict([feats])[0]
