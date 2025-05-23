import subprocess

def speak(text):
    # Voice settings: 'en+f2' for a lighter voice, pitch 80, speed 140
    subprocess.run(["espeak", "-v", "en+f2", "-p", "80", "-s", "170", text])

