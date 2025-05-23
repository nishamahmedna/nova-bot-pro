import tkinter as tk
class NewsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        tk.Label(self, text="News", font=("Arial", 24), bg="white").pack(pady=20)
        tk.Label(self, text="Latest news in the robotics world.", bg="white").pack()
