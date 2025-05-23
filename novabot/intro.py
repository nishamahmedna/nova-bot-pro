import pygame
import time
import os
from speak import speak  # Assuming speak.py is in the same folder or properly imported

def show_intro(screen):
    pygame.mixer.init()

    image_path = "/home/novabot/novabot/assets/novabot_logo.jpeg"
    beep_path = "/home/novabot/novabot/assets/robo_intro.wav"

    # Fill screen with black first
    screen.fill((0, 0, 0))
    pygame.display.update()

    try:
        if os.path.exists(image_path):
            intro_image = pygame.image.load(image_path)
            intro_image = pygame.transform.scale(intro_image, screen.get_size())
            screen.blit(intro_image, (0, 0))
            pygame.display.update()
        else:
            print(f"Image not found at: {image_path}")
    except Exception as e:
        print(f"Error loading image: {e}")

    if os.path.exists(beep_path):
        pygame.mixer.music.load(beep_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    # Use espeak for a kid-like robot voice
    speak("Welcome back to NovaBot")

    time.sleep(3)
