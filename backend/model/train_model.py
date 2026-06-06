import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# ==========================================
# Student Stress Dataset (4 Stress Levels)
# 0 = Low
# 1 = Moderate
# 2 = High
# 3 = Critical
# ==========================================

data = {

    "sleep_hours": [
        8,8.5,7.5,9,8,7.5,8.5,9,8,7.5,
        7,6.5,7,6,6.5,7,6,7,6.5,6,
        5.5,5,4.5,5,4,5.5,4.5,5,4,5,
        3,2.5,3.5,2,3,2.5,3,2,3.5,2
    ],

    "study_hours": [
        2,3,2,1,3,2,1,2,3,2,
        4,5,4,5,4,5,4,5,4,5,
        7,8,7,8,9,7,8,9,8,7,
        10,11,12,10,11,12,10,11,12,10
    ],

    "screen_time": [
        2,3,2,1,2,3,1,2,3,2,
        4,5,4,5,4,5,4,5,4,5,
        6,7,6,7,8,6,7,8,7,6,
        9,10,9,10,11,9,10,11,10,9
    ],

    "exercise_hours": [
        2,2,3,2,3,2,3,2,3,2,
        1.5,1,1.5,1,1.5,1,1.5,1,1.5,1,
        1,0.5,1,0.5,1,0.5,1,0.5,1,0.5,
        0,0,0,0,0,0,0,0,0,0
    ],

    "attendance": [
        95,98,96,99,94,97,95,98,96,97,
        85,88,84,87,86,85,88,84,87,86,
        75,70,72,68,74,70,72,68,74,70,
        60,55,50,58,54,52,60,55,50,58
    ],

    "social_activity": [
        4,5,4,5,4,5,4,5,4,5,
        3,2,3,2,3,2,3,2,3,2,
        1,1,1,1,1,1,1,1,1,1,
        0,0,0,0,0,0,0,0,0,0
    ],

    "academic_pressure": [
        1,2,1,2,1,2,1,2,1,2,
        4,5,4,5,4,5,4,5,4,5,
        7,8,7,8,7,8,7,8,7,8,
        9,10,9,10,9,10,9,10,9,10
    ],

    "stress_level": [
        0,0,0,0,0,0,0,0,0,0,
        1,1,1,1,1,1,1,1,1,1,
        2,2,2,2,2,2,2,2,2,2,
        3,3,3,3,3,3,3,3,3,3
    ]
}

df = pd.DataFrame(data)

X = df.drop("stress_level", axis=1)
y = df["stress_level"]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "stress_model.pkl")

print("✅ stress_model.pkl created successfully!")
print("✅ Model trained successfully!")