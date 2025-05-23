# categories/about.py
import tkinter as tk

class AboutFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        tk.Label(self, text="About", font=("Arial", 24), bg="white").pack(pady=20)
        tk.Label(self, text="Learn more about NovaBot.", bg="white").pack()