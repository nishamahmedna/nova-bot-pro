import tkinter as tk
from frames import load_robot_image

def draw_home_ui(root):
    canvas = tk.Canvas(root, width=1024, height=768, bg="white", highlightthickness=0)
    canvas.place(x=0, y=0)

    robot_img = load_robot_image()
    canvas.create_image(512, 300, image=robot_img)
    canvas.robot_img = robot_img  # Prevent garbage collection

    categories = ["Competitions", "Summer Camps", "Internships", "Workshops", "Exhibitions", "News", "About"]
    x_start, y = 200, 550
    spacing = 120

    for i, category in enumerate(categories):
        x = x_start + (i % 4) * spacing
        y_offset = 50 if i >= 4 else 0
        button = tk.Button(root, text=category, font=("Arial", 12), width=12, bg="#3399ff", fg="white")
        button.place(x=x, y=y + y_offset)
