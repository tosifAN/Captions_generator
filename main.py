
from backend.audio_processing import extract_audio
from backend.speech_to_text import transcribe_audio
from backend.text_summarization import summarize_text
from backend.video_overlay import add_scrolling_text_overlay

def main():
    video_file = 'data/input_video.mp4'
    audio_file = 'data/audio_output.wav'
    processed_video_file = 'data/output_video.mp4'
    
    # Extract audio from video
    extract_audio(video_file, audio_file)
    
    # Transcribe audio to text
    transcript = transcribe_audio(audio_file)
    
    # Optionally summarize the transcript
    summary = summarize_text(transcript)
    
    # Overlay captions on the video
    add_scrolling_text_overlay(video_file, processed_video_file, summary)

if __name__ == "__main__":
    main()
