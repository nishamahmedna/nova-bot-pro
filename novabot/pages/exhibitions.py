# categories/exhibitions.py
import tkinter as tk

class ExhibitionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        tk.Label(self, text="Exhibitions", font=("Arial", 24), bg="white").pack(pady=20)
        tk.Label(self, text="Upcoming robotics exhibitions and showcases.", bg="white").pack()
