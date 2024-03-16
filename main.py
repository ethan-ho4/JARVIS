import os
import queue
import threading
import keyboard
import whisper
import numpy as np
from PIL import Image as im 

from record import record_audio
from transcribe import transcribe_audio


from mistral.mistral_client import mistral
from word_search import word_check

MISTRAL_SERVER_URL = "http://127.0.0.1:5000/v1/chat/completions"
IMAGE_PATH = "feed_images/capture.png"
AUDIO_FILE_PATH = r"audio/recording.wav"

def main():
    audio_directory = "audio"
    os.makedirs(audio_directory, exist_ok=True)

    record_audio()
    transcription = transcribe_audio(AUDIO_FILE_PATH)
    
    mistral_response = mistral(MISTRAL_SERVER_URL,transcription)
    print(mistral_response)

if __name__ == "__main__":
    main()
     