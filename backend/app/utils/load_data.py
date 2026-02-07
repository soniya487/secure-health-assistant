import pandas as pd
from pathlib import Path
BASE = Path(__file__).resolve().parents[2] / "data"

def load_csv(name, fallback_empty=True):
    path = BASE / name
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"[WARN] missing {name}: {e}")
        return pd.DataFrame()

patient_df = load_csv("patient_info.csv")
vitals_df = load_csv("health_vitals.csv")
history_df = load_csv("medical_history.csv")
recommend_df = load_csv("doctor_recommendations.csv")
