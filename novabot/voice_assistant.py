# voice_input.py
from vosk import Model, KaldiRecognizer
import pyaudio
import queue
import json
import os

model_path = "/home/novabot/novabot/model/vosk-model-small-en-us-0.15"
q = queue.Queue()

def recognize_microphone():
    if not os.path.exists(model_path):
        print(f"Model not found at {model_path}")
        return

    model = Model(model_path)
    rec = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()

    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Listening... Speak into your microphone.")

    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "").strip()
            if text:
                q.put(text)
