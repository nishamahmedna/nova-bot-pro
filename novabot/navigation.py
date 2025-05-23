# navigation_buttons.py
import tkinter as tk
from categories.competitions import CompetitionsFrame
from categories.summercamps import SummerCampsFrame
from categories.internships import InternshipsFrame
from categories.workshops import WorkshopsFrame
from categories.exhibitions import ExhibitionsFrame
from categories.news import NewsFrame
from categories.about import AboutFrame

def create_nav_buttons(root, container, show_frame):
    nav_frame = tk.Frame(root, bg="lightgray")
    nav_frame.pack(side="bottom", fill="x")

    buttons = [
        ("Competitions", CompetitionsFrame),
        ("Summer Camps", SummerCampsFrame),
        ("Internships", InternshipsFrame),
        ("Workshops", WorkshopsFrame),
        ("Exhibitions", ExhibitionsFrame),
        ("News", NewsFrame),
        ("About", AboutFrame),
    ]

    for text, frame_class in buttons:
        btn = tk.Button(nav_frame, text=text, font=("Arial", 12), command=lambda fc=frame_class: show_frame(fc, container))
        btn.pack(side="left", padx=10, pady=10)
