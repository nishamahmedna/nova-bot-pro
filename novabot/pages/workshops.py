import tkinter as tk
class WorkshopsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        tk.Label(self, text="Workshops", font=("Arial", 24), bg="white").pack(pady=20)
        tk.Label(self, text="Hands-on robotics workshops and training.", bg="white").pack()
