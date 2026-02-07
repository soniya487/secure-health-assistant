from fastapi import APIRouter, Depends
from app.utils.load_data import vitals_df
from fastapi import Depends

import pandas as pd

router = APIRouter(prefix="/vitals", tags=["Vitals"])

@router.get("/{patient_id}")
def get_patient(patient_id: int):

    if vitals_df.empty:
        return []
    df = vitals_df.copy()
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    latest = df.sort_values("Timestamp", ascending=False).head(1).to_dict(orient="records")
    return latest

@router.get("/alerts")
#def alerts(user=Depends(get_current_user)):
def alerts():
    if vitals_df.empty:
        return []
    alerts = vitals_df[vitals_df["Alert"].astype(str).str.lower() != "normal"]
    return alerts.to_dict(orient="records")
