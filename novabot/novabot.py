import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import messagebox
import threading
import math

# Init speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("NovaBot:", text)
    display_response(text)
    engine.say(text)
    engine.runAndWait()

# GUI window
window = tk.Tk()
window.title("NovaBot")
window.geometry("500x300")
window.configure(bg="black")

title_label = tk.Label(window, text="NovaBot", font=("Helvetica", 24, "bold"), fg="cyan", bg="black")
title_label.pack(pady=10)

output_box = tk.Text(window, height=10, width=60, font=("Courier", 12), bg="black", fg="white")
output_box.pack(pady=10)

def display_user(text):
    output_box.insert(tk.END, f"You: {text}\n")

def display_response(text):
    output_box.insert(tk.END, f"NovaBot: {text}\n")
    output_box.see(tk.END)

def get_response(query):
    query = query.lower()

    if "your name" in query:
        return "I am NovaBot, your robotics buddy."

    elif "sum" in query or "add" in query or "+" in query:
        try:
            numbers = [float(x) for x in query.replace("+", " ").split() if x.replace('.', '', 1).isdigit()]
            return f"The sum is {sum(numbers)}"
        except:
            return "I couldn't calculate that."

    elif "multiply" in query or "*" in query:
        try:
            numbers = [float(x) for x in query.replace("*", " ").split() if x.replace('.', '', 1).isdigit()]
            result = math.prod(numbers)
            return f"The result is {result}"
        except:
            return "I couldn't calculate that."

    elif "what is a sumo bot" in query:
        return "Sumo bots are robots built for battle in a ring. Would you like tutorial, game, ppt, or summer camp?"

    elif query in ["tutorial", "game", "ppt", "summer camp"]:
        return f"Opening {query} page..."  # later we link this to media player

    elif "exit" in query:
        speak("Goodbye!")
        window.quit()

    else:
        return "I don't know that yet."

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        speak("Listening...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        display_user(query)
        reply = get_response(query)
        speak(reply)
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    except sr.RequestError:
        speak("Speech service is unavailable.")

def start_listening():
    threading.Thread(target=listen).start()

listen_button = tk.Button(window, text="🎙️ Speak", command=start_listening, font=("Arial", 14), bg="cyan")
listen_button.pack(pady=20)

speak("NovaBot is ready. Tap the mic and ask me something!")

window.mainloop()
