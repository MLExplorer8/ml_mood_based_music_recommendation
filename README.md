mood_based_music_recommendation_system

This project uses physiological and contextual data (heart rate, skin temperature, blink rate, time of day) to predict a user’s mood and recommend music that matches or improves their emotional state. A clean Streamlit interface enables real-time predictions and recommendations.

🎵 Mood-Based Music Recommender

This project combines a Random Forest Classifier for mood prediction and a recommendation engine for mapping moods to music genres into a single, interactive Streamlit web application. Users can input their data and instantly receive mood-based music suggestions.

🚀 Features

✅ Predicts user mood based on physiological signals

✅ Random Forest Classifier with high accuracy (Train = 0.93, Test = 0.89)

✅ Clean, interactive Streamlit interface

✅ Real-time music recommendations (Happy → Pop, Stressed → Lo-fi)

📂 File Information

train_model.py → Trains the Random Forest model on the dataset

random_forest_model.pkl → Saved trained model

streamlit_app.py → Streamlit application for predictions and recommendations

data/mood_dataset.csv → Dataset used for training
