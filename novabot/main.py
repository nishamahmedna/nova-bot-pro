#main

import pygame
from intro import show_intro
from home import show_home
import cv2  # OpenCV for video playback
import pygame  # Pygame for window and event handling
import os  # For checking files in directories
import queue
import threading
import sounddevice as sd
import json
import vosk
from voice_listener import listen_loop

def start_voice_listener(command_queue):
    listener_thread = threading.Thread(target=listen_loop, args=(command_queue,), daemon=True)
    listener_thread.start()

def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    voice_command_queue = queue.Queue()
    start_voice_listener(voice_command_queue)
    # Play intro
    
    show_intro(screen)
    
    show_home(screen, voice_command_queue)

    # Keep home visible until user exits
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
