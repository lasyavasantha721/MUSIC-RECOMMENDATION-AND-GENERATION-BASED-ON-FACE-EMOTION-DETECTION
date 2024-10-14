# Music Recommendation and Generation Based on Face Emotion Detection

## Project Overview

This project develops a system that leverages facial emotion recognition to recommend and generate personalized music tracks. By analyzing the user's facial expressions in real-time, the system tailors music recommendations to match their emotional state, enhancing the overall listening experience.

## Features

- **Emotion Detection:** Uses Convolutional Neural Networks (CNN) and ResNet50 to detect facial emotions from webcam input.
- **Music Recommendation:** Employs a recommendation algorithm to suggest music tracks based on detected emotions.
- **Music Generation:** Integrates Long Short-Term Memory (LSTM) models to generate personalized music sequences according to the user's mood.

## Tech Stack

- **Frontend:** Python (OpenCV) for real-time emotion detection.
- **Backend:** Python with TensorFlow/Keras for emotion recognition and music generation.
- **Models:** CNN, ResNet50 for emotion detection; LSTM for music generation.
- **Libraries:** OpenCV, TensorFlow/Keras, NumPy, Pandas.
- **Data:** Facial emotion datasets and music tracks.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Vishnu287345/music-recommendation-emotion-detection.git
   cd music-recommendation-emotion-detection
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Pre-trained Models:**
   Download the pre-trained models for emotion detection and music generation from [link-to-models] and place them in the `models/` directory.

## Usage

1. **Run Emotion Detection:**
   ```bash
   python emotion_detection.py
   ```

2. **Generate Music Recommendations:**
   Based on detected emotions, music recommendations will be provided in the application.

3. **Generate Music:**
   ```bash
   python music_generation.py
   ```

## Examples

- **Emotion Detection Interface:** A live video feed showing detected emotions.
- **Music Recommendation Output:** A list of recommended tracks based on the current emotion.
- **Generated Music:** Example audio sequences generated based on detected emotions.
