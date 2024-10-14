import streamlit as st
import os
import pretty_midi
from pydub import AudioSegment
midi_file = open('generated.mid', 'rb')
midi_data = midi_file
midi_data = pretty_midi.PrettyMIDI(midi_data)
audio_data = midi_data.fluidsynth()





st.audio(audio_data, format='audio/wav')