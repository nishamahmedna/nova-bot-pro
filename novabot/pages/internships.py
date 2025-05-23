# categories/internships.py
import tkinter as tk

class InternshipsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        tk.Label(self, text="Internships", font=("Arial", 24), bg="white").pack(pady=20)
        tk.Label(self, text="Discover internship opportunities in robotics.", bg="white").pack()