
import streamlit as st
from src.predict import predict_marks

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Performance Prediction")
st.write(
    "Enter the student's details to estimate final exam marks."
)

study_hours = st.number_input(
    "Daily study hours",
    min_value=0.0,
    max_value=24.0,
    value=4.0,
    step=0.5
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=80.0,
    step=1.0
)

previous_marks = st.number_input(
    "Previous exam marks (out of 100)",
    min_value=0.0,
    max_value=100.0,
    value=65.0,
    step=1.0
)

if st.button("Predict Final Marks"):
    result = predict_marks(
        study_hours,
        attendance,
        previous_marks
    )

    st.success(f"Predicted final marks: {result}/100")
    st.caption(
        "This is an educational estimate based on illustrative sample data, "
        "not a guaranteed exam result."
    )
