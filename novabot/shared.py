# shared.py

import pygame
import sys
import time
import threading
from ffpyplayer.player import MediaPlayer

latest_voice_command = ""

def render_voice_command(screen, command_text):
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render(f"Voice Command: {command_text}", True, (255, 255, 255))
    screen.blit(text_surface, (20, screen.get_height() - 40))

def play_video(screen, video_path, background_image=None, voice_command_queue=None):
    global latest_voice_command

    screen_width, screen_height = screen.get_size()
    frame_width, frame_height = 800, 450
    x = (screen_width - frame_width) // 2
    y = (screen_height - frame_height) // 2

    pygame.display.set_caption("Playing Video")
    clock = pygame.time.Clock()
    player = MediaPlayer(video_path)

    close_button_size = 30
    close_rect = pygame.Rect(x + frame_width - close_button_size - 10, y + 10, close_button_size, close_button_size)

    playing = True
    paused = False

    def monitor_voice_commands():
        nonlocal playing, paused
        while playing:
            if voice_command_queue and not voice_command_queue.empty():
                command = voice_command_queue.get().lower()
                latest_voice_command = command
                if command in ("back", "stop", "close", "exit"):
                    playing = False
            time.sleep(0.1)

    if voice_command_queue:
        threading.Thread(target=monitor_voice_commands, daemon=True).start()

    while playing:
        if not paused:
            frame, val = player.get_frame()
        else:
            frame, val = None, None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.close_player()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                player.close_player()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if close_rect.collidepoint(event.pos):
                    player.close_player()
                    return

        if background_image:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill((0, 0, 0))

        if val == 'eof':
            break

        if frame is not None:
            img, t = frame
            frame_surface = pygame.image.frombuffer(img.to_bytearray()[0], img.get_size(), 'RGB')
            frame_surface = pygame.transform.scale(frame_surface, (frame_width, frame_height))
            pygame.draw.rect(screen, (255, 255, 255), (x - 4, y - 4, frame_width + 8, frame_height + 8))
            screen.blit(frame_surface, (x, y))

        pygame.draw.rect(screen, (200, 0, 0), close_rect)
        font = pygame.font.SysFont(None, 24)
        text = font.render('X', True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=close_rect.center))

        render_voice_command(screen, latest_voice_command)

        pygame.display.flip()
        clock.tick(30)

    player.close_player()

