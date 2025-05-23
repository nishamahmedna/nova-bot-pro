import pyttsx3
from pydub import AudioSegment
from pydub.effects import low_pass_filter, normalize

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 140)  # Slower speech
engine.save_to_file("Welcome to NovaBot", "tts_raw.wav")
engine.runAndWait()

# Load and process
sound = AudioSegment.from_wav("tts_raw.wav")
sound = normalize(sound)                       # Normalize volume
sound = low_pass_filter(sound, cutoff=1500)    # Robotic tone

# Save final version
sound.export("tts_welcome.wav", format="wav")
print("✅ Robotic welcome voice generated as tts_welcome.wav")
