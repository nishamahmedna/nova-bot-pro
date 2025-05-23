import tkinter as tk
import random
import time
import threading
from PIL import Image, ImageTk
import os

# Set path to images
FRAME_DIR = "assets/robot_anim_frames"

class RobotAnimator:
    def __init__(self, canvas):
        self.canvas = canvas
        self.frames = self.load_frames()
        self.current_frame = 0
        self.image_on_canvas = self.canvas.create_image(512, 384, image=self.frames[0])
        self.running = True
        self.lip_sync_active = False

        self.blink_thread = threading.Thread(target=self.blink_loop, daemon=True)
        self.eye_thread = threading.Thread(target=self.eye_movement_loop, daemon=True)
        self.anim_thread = threading.Thread(target=self.animate_loop, daemon=True)

        self.blink_thread.start()
        self.eye_thread.start()
        self.anim_thread.start()

    def load_frames(self):
        frame_files = sorted([
            f for f in os.listdir(FRAME_DIR)
            if f.endswith(".png")
        ])
        return [ImageTk.PhotoImage(Image.open(os.path.join(FRAME_DIR, f)).resize((1024, 768))) for f in frame_files]

    def animate_loop(self):
        while self.running:
            if self.lip_sync_active:
                for frame in self.frames:
                    self.canvas.itemconfig(self.image_on_canvas, image=frame)
                    time.sleep(0.1)
            else:
                self.canvas.itemconfig(self.image_on_canvas, image=self.frames[0])  # Default face
            time.sleep(0.1)

    def blink_loop(self):
        while self.running:
            if not self.lip_sync_active:
                time.sleep(random.randint(3, 7))
                self.canvas.itemconfig(self.image_on_canvas, image=self.frames[1])  # Blink frame
                time.sleep(0.2)
                self.canvas.itemconfig(self.image_on_canvas, image=self.frames[0])  # Back to normal

    def eye_movement_loop(self):
        while self.running:
            if not self.lip_sync_active:
                time.sleep(random.randint(4, 8))
                self.canvas.itemconfig(self.image_on_canvas, image=self.frames[2])  # Eye move
                time.sleep(0.3)
                self.canvas.itemconfig(self.image_on_canvas, image=self.frames[0])  # Back to normal

    def start_lip_sync(self):
        self.lip_sync_active = True

    def stop_lip_sync(self):
        self.lip_sync_active = False

    def stop(self):
        self.running = False


# Instance control for access from main
animator_instance = None

def setup_animator(canvas):
    global animator_instance
    animator_instance = RobotAnimator(canvas)

def start_lip_sync():
    if animator_instance:
        animator_instance.start_lip_sync()

def stop_lip_sync():
    if animator_instance:
        animator_instance.stop_lip_sync()
