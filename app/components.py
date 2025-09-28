# # components.py
# import pandas as pd
# import plotly.graph_objects as go
# import plotly.express as px

# def workload_gauge(value):
#     """
#     value: numeric (expected 0..2 or similar). We clamp & map to 0-2 for gauge.
#     """
#     try:
#         v = float(value)
#     except Exception:
#         v = 0.0
#     # clamp to [0, 2]
#     v = max(0.0, min(2.0, v))
#     fig = go.Figure(go.Indicator(
#         mode="gauge+number",
#         value=v,
#         title={"text": "Mental Workload"},
#         gauge={
#             "axis": {"range": [0, 2], "tickvals": [0, 1, 2], "ticktext": ["Low", "Med", "High"]},
#             "bar": {"color": "blue"},
#             "steps": [
#                 {"range": [0, 0.9], "color": "#d6f5d6"},
#                 {"range": [0.9, 1.5], "color": "#fff2cc"},
#                 {"range": [1.5, 2], "color": "#ffd6d6"},
#             ],
#         }
#     ))
#     fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), height=350)
#     return fig

# def accuracy_line(df: pd.DataFrame):
#     """
#     df must contain columns: 'time' and 'accuracy'
#     """
#     if df is None or df.empty:
#         # return a blank figure
#         fig = go.Figure()
#         fig.update_layout(title="Accuracy Probability Over Time")
#         return fig
#     fig = px.line(df, x="time", y="accuracy", title="Accuracy Probability Over Time", markers=True)
#     fig.add_hline(y=0.5, line_dash="dash", line_color="red", annotation_text="Threshold 0.5", annotation_position="top left")
#     fig.update_yaxes(range=[0, 1], title_text="Probability")
#     fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), height=350)
#     return fig

# def emotion_timeline(df: pd.DataFrame):
#     """
#     df columns: start, end, emotion
#     If only one row, px.timeline can still render but we ensure correct types.
#     """
#     if df is None or df.empty:
#         # return blank figure
#         fig = go.Figure()
#         fig.update_layout(title="Emotion Transitions By Time")
#         return fig

#     # Ensure numeric columns
#     df = df.copy()
#     df["start"] = pd.to_numeric(df["start"], errors="coerce").fillna(0)
#     df["end"] = pd.to_numeric(df["end"], errors="coerce").fillna(df["start"] + 1)
#     df["emotion"] = df["emotion"].astype(str)

#     fig = px.timeline(df, x_start="start", x_end="end", y="emotion", color="emotion", title="Emotion Transitions By Time")
#     fig.update_yaxes(autorange="reversed")  # keep timeline top-down
#     fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), height=350)
#     return fig

# components.py
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def workload_gauge(value):
    try:
        v = float(value)
    except Exception:
        v = 0.0
    v = max(0.0, min(2.0, v))  # clamp
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=v,
        title={"text": "Mental Workload"},
        gauge={
            "axis": {"range": [0, 2], "tickvals": [0, 1, 2], "ticktext": ["Low", "Med", "High"]},
            "bar": {"color": "blue"},
            "steps": [
                {"range": [0, 0.9], "color": "#d6f5d6"},
                {"range": [0.9, 1.5], "color": "#fff2cc"},
                {"range": [1.5, 2], "color": "#ffd6d6"},
            ],
        }
    ))
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), height=350)
    return fig

def accuracy_line(df: pd.DataFrame):
    if df is None or df.empty:
        fig = go.Figure()
        fig.update_layout(title="Accuracy Probability Over Time")
        return fig
    fig = px.line(df, x="time", y="accuracy", title="Accuracy Probability Over Time", markers=True)
    fig.add_hline(y=0.5, line_dash="dash", line_color="red",
                  annotation_text="Threshold 0.5", annotation_position="top left")
    fig.update_yaxes(range=[0, 1], title_text="Probability")
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), height=350)
    return fig

def emotion_timeline(df: pd.DataFrame):
    if df is None or df.empty:
        fig = go.Figure()
        fig.update_layout(title="Emotion Transitions By Time")
        return fig
    df = df.copy()
    df["start"] = pd.to_numeric(df["start"], errors="coerce").fillna(0)
    df["end"] = pd.to_numeric(df["end"], errors="coerce").fillna(df["start"] + 1)
    df["emotion"] = df["emotion"].astype(str)
    fig = px.timeline(df, x_start="start", x_end="end", y="emotion", color="emotion",title="Emotion Transitions By Time")
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), height=350)
    return fig
