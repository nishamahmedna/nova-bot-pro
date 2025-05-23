# frames.py
import tkinter as tk

def setup_main_frames(root):
    container = tk.Frame(root, bg="white")
    container.pack(fill="both", expand=True)
    return container

def show_frame(frame_class, container):
    for widget in container.winfo_children():
        widget.destroy()
    frame = frame_class(container)
    frame.pack(fill="both", expand=True)
