import tkinter as tk
from tkinter import ttk

class NovaBotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NovaBot")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#121212")

        self.title = tk.Label(root, text="🤖 NovaBot", font=("Arial", 32, "bold"), fg="white", bg="#121212")
        self.title.pack(pady=20)

        self.user_label = tk.Label(root, text="", font=("Arial", 20), fg="#00ffcc", bg="#121212", wraplength=1000)
        self.user_label.pack(pady=10)

        self.bot_label = tk.Label(root, text="", font=("Arial", 20), fg="#ffcc00", bg="#121212", wraplength=1000)
        self.bot_label.pack(pady=10)

    def display_user_text(self, text):
        self.user_label.config(text="You: " + text)

    def display_bot_text(self, text):
        self.bot_label.config(text="NovaBot: " + text)
