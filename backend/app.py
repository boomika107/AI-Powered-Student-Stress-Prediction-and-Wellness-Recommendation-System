from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
import sqlite3
from datetime import datetime
from flask import jsonify

app = Flask(__name__)

model = joblib.load("stress_model.pkl")


# ==========================
# DATABASE CREATION
# ==========================

def init_db():

    conn = sqlite3.connect("stress_history.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stress_level TEXT,
            wellness_score INTEGER,
            prediction_date TEXT
        )
    """)

    conn.commit()
    conn.close()


init_db()


# ==========================
# HOME PAGE
# ==========================

@app.route('/')
def home():

    conn = sqlite3.connect("stress_history.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM predictions
        ORDER BY id DESC
    """)

    history = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        prediction=None,
        history=history
    )


# ==========================
# API ENDPOINT
# ==========================

@app.route('/predict', methods=['POST'])
def predict():

    try:

        data = request.get_json()

        features = np.array([[
            data['sleep_hours'],
            data['study_hours'],
            data['screen_time'],
            data['exercise_hours'],
            data['attendance'],
            data['social_activity'],
            data['academic_pressure']
        ]])

        prediction = int(model.predict(features)[0])

        return jsonify({
            "prediction": prediction
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================
# FRONTEND FORM PREDICTION
# ==========================

@app.route('/predict_form', methods=['POST'])
def predict_form():

    try:

        features = np.array([[

            float(request.form['sleep_hours']),
            float(request.form['study_hours']),
            float(request.form['screen_time']),
            float(request.form['exercise_hours']),
            float(request.form['attendance']),
            float(request.form['social_activity']),
            float(request.form['academic_pressure'])

        ]])

        prediction = int(model.predict(features)[0])

        print("Prediction =", prediction)

        # ==========================
        # LOW STRESS
        # ==========================

        if prediction == 0:

            category = "🟢 Low Stress"
            color = "#28a745"
            emotion_image = "low_stress.png"

            recommendation = """
✔ Maintain your healthy routine
✔ Continue regular exercise
✔ Keep balanced study habits
✔ Stay socially active
"""

            wellness_score = 95

        # ==========================
        # MODERATE STRESS
        # ==========================

        elif prediction == 1:

            category = "🟡 Moderate Stress"
            color = "#ffc107"
            emotion_image = "moderate_stress.png"

            recommendation = """
✔ Take short study breaks
✔ Improve sleep schedule
✔ Practice relaxation techniques
✔ Manage daily tasks effectively
"""

            wellness_score = 75

        # ==========================
        # HIGH STRESS
        # ==========================

        elif prediction == 2:

            category = "🟠 High Stress"
            color = "#fd7e14"
            emotion_image = "high_stress.png"

            recommendation = """
✔ Reduce screen time
✔ Follow a structured study plan
✔ Practice meditation and deep breathing
✔ Talk with friends, mentors or family
"""

            wellness_score = 50

        # ==========================
        # CRITICAL STRESS
        # ==========================

        else:

            category = "🔴 Critical Stress"
            color = "#dc3545"
            emotion_image = "critical_stress.png"

            recommendation = """
✔ Seek professional counseling support
✔ Take immediate rest and recovery time
✔ Contact trusted family members
✔ Prioritize mental wellness immediately
"""

            wellness_score = 25

        # ==========================
        # SAVE TO DATABASE
        # ==========================

        conn = sqlite3.connect("stress_history.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO predictions
            (stress_level, wellness_score, prediction_date)
            VALUES (?, ?, ?)
            """,
            (
                category,
                wellness_score,
                datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            )
        )

        conn.commit()

        # ==========================
        # FETCH HISTORY
        # ==========================

        cursor.execute("""
            SELECT *
            FROM predictions
            ORDER BY id DESC
        """)

        history = cursor.fetchall()

        conn.close()

        return render_template(

            "index.html",

            prediction=prediction,
            category=category,
            color=color,
            recommendation=recommendation,
            wellness_score=wellness_score,
            emotion_image=emotion_image,
            history=history

        )

    except Exception as e:

        print("ERROR:", str(e))

        return render_template(

            "index.html",

            prediction=None,
            recommendation=str(e)

        )


# ==========================
# RUN APP
# ==========================

if __name__ == '__main__':
    app.run(debug=True)