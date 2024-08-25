import speech_recognition as sr
from pydub import AudioSegment
import os

def split_audio(audio_file_path, chunk_length_ms=5000):
    """Split audio file into chunks of specified length."""
    audio = AudioSegment.from_wav(audio_file_path)
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk_file = f"{audio_file_path}_chunk_{i // chunk_length_ms}.wav"
        chunk.export(chunk_file, format='wav')
        chunks.append(chunk_file)
    return chunks


def convert_audio_to_wav(audio_file_path):
    """Convert audio file to WAV format."""
    audio = AudioSegment.from_file(audio_file_path)
    wav_file_path = audio_file_path.replace('.mp3', '.wav')
    audio.export(wav_file_path, format='wav')
    return wav_file_path

def transcribe_audio(audio_file_path):
    """Transcribe audio file to text."""
    recognizer = sr.Recognizer()
    
    # Convert to WAV if needed
    if not audio_file_path.lower().endswith('.wav'):
        audio_file_path = convert_audio_to_wav(audio_file_path)

    transcript = ""
    chunks = split_audio(audio_file_path)
    
    for chunk in chunks:
        with sr.AudioFile(chunk) as source:
            try:
                audio_data = recognizer.record(source)
                chunk_transcript = recognizer.recognize_google(audio_data)
                transcript += chunk_transcript + " "
            except sr.UnknownValueError:
                transcript += "[Could not understand audio] "
            except sr.RequestError as e:
                transcript += f"[Error: {e}] "
    
    # Clean up chunk files
    for chunk in chunks:
        os.remove(chunk)
    # Clean up WAV file if it was created
    if audio_file_path.lower().endswith('.wav'):
        os.remove(audio_file_path)
   
    print("######################################")
    print("my transcript: ", transcript)
    print("######################################")   
    return transcript
