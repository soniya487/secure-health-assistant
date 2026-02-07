from fastapi import APIRouter, Depends
from app.utils.load_data import patient_df, history_df, recommend_df
from app.utils.auth import get_current_user

router = APIRouter(prefix="/patient", tags=["Patient"])

@router.get("/all")
def get_all(user=Depends(get_current_user)):
    # RBAC check: doctors & admin & patient allowed (patients see their own)
    # In this demo return all if doctor/admin; patient sees their own info
    role = user.get("role")
    if role in ["doctor","admin"]:
        return patient_df.to_dict(orient="records")
    elif role == "patient":
        # find patient by username mapping (demo)
        pid = 2  # demo map
        info = patient_df[patient_df["PatientID"]==pid].to_dict(orient="records")
        return info
    else:
        return {"error":"insufficient privileges"}

@router.get("/{patient_id}")
def get_patient(patient_id: int, user=Depends(get_current_user)):
    # allow only doctor/admin or same patient
    role = user.get("role")
    if role in ["doctor","admin"]:
        info = patient_df[patient_df["PatientID"]==patient_id].to_dict(orient="records")
        history = history_df[history_df["PatientID"]==patient_id].to_dict(orient="records")
        rec = recommend_df[recommend_df["PatientID"]==patient_id].to_dict(orient="records")
        return {"info":info,"history":history,"recommendations":rec}
    if role == "patient":
        # demo patient id mapping for demo user
        return {"error":"patients can only view their own data in demo"}
    return {"error":"forbidden"}
