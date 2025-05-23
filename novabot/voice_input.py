# voice_listener.py
import queue
import sounddevice as sd
import vosk
import json
import os

MODEL_PATH = "/home/novabot/novabot/model/vosk-model-small-en-us-0.15"

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def listen_loop(command_queue):
    if not os.path.exists(MODEL_PATH):
        print("Model not found!")
        return

    model = vosk.Model(MODEL_PATH)
    samplerate = 16000

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening for voice commands...")
        rec = vosk.KaldiRecognizer(model, samplerate)

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print(f"[Voice Input] {text}")
                    command_queue.put(text)
