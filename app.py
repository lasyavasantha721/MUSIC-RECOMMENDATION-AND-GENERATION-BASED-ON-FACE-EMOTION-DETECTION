import streamlit as st
from streamlit.components.v1 import components
from PIL import Image
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from recom import *
from PIL import Image
from test_music import *
emotion_model = load_model('resnet_model')
def detect_emotion(img):
    
    emotion_model = load_model('resnet_model')
    
    frame = cv2.resize(img, (128, 128))
    face_detector = cv2.CascadeClassifier('frontalface.xml')
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
    
    for (x,y,w,h) in num_faces:
        cv2.rectangle(frame, (x,y-50), (x+w, y+h+10), (0,255,0), 4)
        roi_gray_frame = gray_frame[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
        
        emotion_prediction = emotion_model.predict(cropped_img)
        maxindex = int(np.argmax(emotion_prediction))
        cv2.putText(frame, emotion_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        
        
    return frame, maxindex
    
   
    
if __name__=='__main__':

    st.title("Music Recommender System")
    
    emotion_dict = {0: "Angry", 1: "Disgusted", 3: "Normal", 2: "Fearful", 4: "Happy", 5: "Sad", 6: "Surprised"}
    track_url = "https://open.spotify.com/track/12342"
    img_file_buffer = st.camera_input("Capture")
    if img_file_buffer is not None:
        if img_file_buffer is not None:
            image = Image.open(img_file_buffer)
            image = image.resize((128, 128))
            cv2_img = np.array(image)
            cv2_img = np.reshape(cv2_img,(1, 128, 128, 3))
            prediction = emotion_model.predict(cv2_img)
            index = np.argmax(prediction)
            st.write("Detected Emotion: "+emotion_dict[index])
                
            if st.button('Recommend Music and generate music'):
                tracks = recom_song(emotion_dict[index])
                for track in tracks:
                    st.write(f'Link to Track" {track}')
                
                _, _, _ = Malody_Generator(100)
                with open('generated.midi', 'rb') as f:
                    st.download_button('Download midi', f, file_name='generated.midi')
        # try:
            # if img_file_buffer is not None:
            #     image = Image.open(img_file_buffer)
            #     cv2_img = np.array(image)
            #     img, id = detect_emotion(cv2_img)
                
            # st.write("Detected Emotion: "+emotion_dict[id])
                
            # if st.button('Recommend Music and generate music'):
            #     tracks = recom_song(emotion_dict[id])
            #     for track in tracks:
            #         st.write(f'Link to Track" {track}')
                
            #     _, _, _ = Malody_Generator(100)
            #     with open('generated.midi', 'rb') as f:
            #         st.download_button('Download midi', f, file_name='generated.midi')
                        
        # except:
        #     st.write("Listen To this musics:")
        #     st.write("https://open.spotify.com/track/12342")
        #     st.write("https://open.spotify.com/track/55332")
        #     _, _, _ = Malody_Generator(100)
        #     with open('generated.midi', 'rb') as f:
        #         st.download_button('Download midi', f, file_name='generated.midi')
        
        
