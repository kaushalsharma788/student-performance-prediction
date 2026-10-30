
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model/student_model.pkl")


def predict_marks(study_hours, attendance, previous_marks):
    """Predict final exam marks using the trained model."""

    if study_hours < 0 or study_hours > 24:
        raise ValueError("Study hours must be between 0 and 24.")

    if not 0 <= attendance <= 100:
        raise ValueError("Attendance must be between 0 and 100.")

    if not 0 <= previous_marks <= 100:
        raise ValueError("Previous marks must be between 0 and 100.")

    student = pd.DataFrame([{
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_marks": previous_marks
    }])

    prediction = model.predict(student)[0]

    # Keep displayed marks within the 0–100 range
    return round(max(0, min(100, prediction)), 2)


if __name__ == "__main__":
    print("\nSTUDENT PERFORMANCE PREDICTION")
    print("-" * 35)

    try:
        hours = float(input("Daily study hours: "))
        attendance = float(input("Attendance percentage: "))
        previous = float(input("Previous exam marks (out of 100): "))

        result = predict_marks(hours, attendance, previous)

        print(f"\nPredicted final marks: {result}/100")

    except ValueError as error:
        print("Invalid input:", error)

