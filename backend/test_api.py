import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "sleep_hours": 5,
    "study_hours": 8,
    "screen_time": 6,
    "exercise_hours": 1,
    "attendance": 85,
    "social_activity": 3,
    "academic_pressure": 7
}

try:
    response = requests.post(url, json=data)

    print("Status Code:", response.status_code)
    print("Response Text:")
    print(response.text)

except Exception as e:
    print("Error:", e)