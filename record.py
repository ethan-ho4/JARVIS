import os
import pyaudio
import wave
import numpy as np
import keyboard

def rms_to_db(rms):
    return 20 * np.log10(rms)

def calculate_rms(data):
    # Convert byte data to numpy array of type int16
    audio_data = np.frombuffer(data, dtype=np.int16)
    
    # Calculate RMS
    rms = np.sqrt(np.mean(np.square(audio_data), axis=0))
    return rms

def record_audio(RECORDING="recording.wav", silence_limit=3):
    # Parameters for recording
    FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
    CHANNELS = 1  # Number of audio channels
    RATE = 44100  # Sample rate (samples per second)
    CHUNK = 1024  # Number of frames per buffer
    SILENCE_THRESHOLD = -40  # Silence threshold in dB

    # Directory where the recording will be saved
    RECORDING_DIR = "audio"
    
    # Full path for the recording
    recording_path = os.path.join(RECORDING_DIR, RECORDING)

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open stream for recording
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording... (press spacebar to stop)")

    frames = []
    silent_chunks = 0
    silence_reached = False

    # while not silence_reached and not keyboard.is_pressed('space'):
    while not silence_reached and not keyboard.is_pressed('space'):
        data = stream.read(CHUNK)
        rms_val = calculate_rms(data)
        db_val = rms_to_db(rms_val)

        if db_val < SILENCE_THRESHOLD:
            silent_chunks += 1
            if silent_chunks >= silence_limit * RATE / CHUNK:
                silence_reached = True
        else:
            silent_chunks = 0
            frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(recording_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"Recording saved to {recording_path}")

