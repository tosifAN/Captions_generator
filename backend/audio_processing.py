import subprocess

def extract_audio(video_file_path, audio_file_path):
    command = [
    'ffmpeg', '-i', video_file_path, '-q:a', '0', '-map', 'a', audio_file_path
    ]
    subprocess.run(command, check=True)

