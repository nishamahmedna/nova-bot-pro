# categories/summercamps.py
import tkinter as tk

class SummerCampsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        tk.Label(self, text="Summer Camps", font=("Arial", 24), bg="white").pack(pady=20)
        tk.Label(self, text="Explore exciting robotics summer camps.", bg="white").pack()
