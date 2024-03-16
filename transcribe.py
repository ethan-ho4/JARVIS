import whisper

def transcribe_audio(file_path):
    # Load the Whisper model
    model = whisper.load_model("base")

    # Process the audio file and output the result
    result = model.transcribe(file_path)
    
    # Extract the transcription text
    transcription = result["text"]
    
    print("Transcription:")
    print(transcription)
    
    return transcription
