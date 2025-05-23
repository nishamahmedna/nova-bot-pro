import pyttsx3
import time

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[16].id)  # replace KID_INDEX with actual index
engine.setProperty('rate', 150)  # optional: adjust speed
engine.say("Welcome back to NovaBot")
engine.runAndWait()
time.sleep(3)
