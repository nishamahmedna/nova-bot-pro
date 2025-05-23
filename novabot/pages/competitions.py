import tkinter as tk

class CompetitionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        tk.Label(self, text="Competitions", font=("Arial", 24), bg="white").pack(pady=20)
        tk.Label(self, text="Here you'll find competition details.", bg="white").pack()
