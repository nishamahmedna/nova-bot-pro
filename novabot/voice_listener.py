import queue
import sounddevice as sd
import vosk
import json
import os

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def listen_loop(command_queue):
    model_path = "/home/novabot/novabot/model/vosk-model-small-en-us-0.15"
    if not os.path.exists(model_path):
        print("Model not found!")
        return

    model = vosk.Model(model_path)
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
                    
def listen_once():
    model = vosk.Model("model")
    recognizer = vosk.KaldiRecognizer(model, 16000)
    stream = sd.InputStream(samplerate=16000, channels=1)
    stream.start()
    print("Listening...")

    result = ""
    start_time = time.time()

    while time.time() - start_time < 6:  # max listen time
        data, _ = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            result = json.loads(text).get("text", "")
            break

    stream.stop()
    return result

