import streamlit as st
import joblib
import numpy as np

# Load the trained Random Forest model
model = joblib.load(r'D:\your_file_path\random_forest_model.pkl')

# Define possible moods and music recommendations
mood_music = {
    'Happy': 'Upbeat Pop Playlist',
    'Sad': 'Soothing Acoustic Playlist',
    'Relaxed': 'Chill Instrumental Playlist',
    'Stressed': 'Calm Piano Playlist'
}

# Streamlit UI
st.title('Mood-Based Music Recommendation System')
st.write('Adjust the sliders to input your physiological features:')

heart_rate = st.slider('Heart Rate', 40, 180, 70)
skin_temp = st.slider('Skin Temperature', 30.0, 40.0, 36.5)
blink_rate = st.slider('Blink Rate', 5, 60, 20)
time_of_day = st.selectbox('Time of Day', ['Morning', 'Afternoon', 'Evening', 'Night'])

# Encode Time of Day as in training
time_of_day_map = {'Morning': 0, 'Afternoon': 1, 'Evening': 2, 'Night': 3}
time_of_day_code = time_of_day_map[time_of_day]

# Prepare input for prediction
features = np.array([[heart_rate, skin_temp, blink_rate, time_of_day_code]])
predicted_mood = model.predict(features)[0]
st.subheader(f'Predicted Mood: {predicted_mood}')
recommendation = mood_music.get(predicted_mood, 'Enjoy your favorite music!')
st.success(f'Recommended Music: {recommendation}')
