# AI-Powered Student Stress Prediction and Wellness Recommendation System

## Objective
To predict student stress levels using Machine Learning and provide personalized wellness recommendations.

## Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python Flask

### Machine Learning
- Scikit-Learn

### Database
- SQLite

### Model Storage
- Joblib (.pkl)

## Project Workflow

Student Data
↓
Data Preprocessing
↓
Machine Learning Model
↓
Stress Prediction
↓
Recommendation Engine
↓
Wellness Suggestions
+----------------+
|    STUDENT     |
+----------------+
| Student_ID (PK)|
| Name           |
| Age            |
| Gender         |
| Department     |
| Year           |
+----------------+
         |
         | 1
         |
         | M+----------------+
            |    Student     |
            +----------------+
                    |
     --------------------------------
     |              |              |
     v              v              v
 Enter Data   View Result   Get Suggestions

                    |
                    v

            +----------------+
            | AI Prediction  |
            |    System      |
            +----------------++------------+
|   Student  |
+------------+
      |
      v
+------------------+
| Flask Web App    |
+------------------+
      |
      v
+------------------+
| Input Processing |
+------------------+
      |
      v
+------------------+
| ML Model         |
| (Random Forest)  |
+------------------+
      |
      v
+------------------+
| Prediction       |
+------------------+
      |
      v
+------------------+
| Result Display   |
+------------------+
+--------------------+
| STRESS_ASSESSMENT  |
+--------------------+
| Assessment_ID (PK) |
| Student_ID (FK)    |
| Sleep_Hours        |
| Study_Hours        |
| Academic_Pressure  |
| Social_Support     |
| Financial_Stress   |
| Anxiety_Level      |
| Stress_Level       |
| Prediction_Date    |
+--------------------+
         |
         | 1
         |
         | 1
+-------------------+
|   PREDICTION      |
+-------------------+
| Prediction_ID(PK) |
| Assessment_ID(FK) |
| Predicted_Result  |
| Confidence_Score  |
+-------------------+