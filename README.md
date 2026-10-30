
# Student Performance Prediction Using Machine Learning

## About the Project

This project predicts a student's final examination marks using
Machine Learning.

It uses three input features:

- Daily study hours
- Attendance percentage
- Previous examination marks

The project uses the Linear Regression algorithm.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit

## Project Structure

```text
student performance prediction/
├── dataset/
│   └── student_performance.csv
├── model/
│   └── student_model.pkl
├── reports/
│   └── project_report.docx
├── src/
│   ├── __init__.py
│   ├── predict.py
│   └── train_model.py
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/kaushalsharma788/student-performance-prediction.git
```

Move into the project folder:

```bash
cd student-performance-prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Train the Model

```bash
python src/train_model.py
```

## Run the Prediction Application

```bash
streamlit run app.py
```

## Machine Learning Algorithm

Linear Regression is used to estimate final exam marks
based on the student's input features.

## Dataset

The project currently uses an illustrative sample dataset
for educational demonstration.

It does not represent actual student records.

## Disclaimer

Predictions are estimates and should not be used to make
high-stakes academic decisions.

## Author

Kaushal Sharma

## Future Improvements

- Use a larger real-world dataset with appropriate permission.
- Compare multiple machine learning algorithms.
- Improve model evaluation.
- Add visualizations and student performance analytics.

