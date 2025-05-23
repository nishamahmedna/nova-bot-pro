import os
import json
import pygame
from shared import play_video, render_voice_command

PAGES = {
    "Tutorials": "/home/novabot/novabot/pages/tutorials",
    "Competitions": "/home/novabot/novabot/pages/competitions",
    "Workshops": "/home/novabot/novabot/pages/workshops",
    "Exhibitions": "/home/novabot/novabot/pages/exhibitions",
    "Summer Camps": "/home/novabot/novabot/pages/summer_camps",
    "Internships": "/home/novabot/novabot/pages/internships",
    "News": "/home/novabot/novabot/pages/news",
    "About": "/home/novabot/novabot/pages/about"
}

def generate_thumbnail(video_path):
    import cv2
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        return None
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
    return pygame.transform.scale(surface, (200, 120))

def show_search_page(screen, bg_image, voice_command_queue):
    font = pygame.font.SysFont(None, 24)
    title_font = pygame.font.SysFont(None, 36)
    small_font = pygame.font.SysFont(None, 20)
    matched_videos = []
    latest_voice_command = ""
    listening = True  # New flag

    def search_videos(keyword):
        results = []
        for category, folder in PAGES.items():
            metadata_file = os.path.join(folder, "metadata.json")
            if os.path.exists(metadata_file):
                with open(metadata_file, "r") as f:
                    videos = json.load(f)
                    for video in videos:
                        if keyword in video["title"].lower() or keyword in video["description"].lower():
                            video["path"] = os.path.join(folder, video["file"])
                            results.append(video)
        return results

    thumb_rects = []
    running = True

    while running:
        screen.blit(bg_image, (0, 0))
        thumb_rects.clear()

        # --- Draw BACK button ---
        back_button_rect = pygame.Rect(20, 20, 100, 40)
        pygame.draw.rect(screen, (70, 130, 180), back_button_rect, border_radius=8)
        back_text = font.render("Back", True, (255, 255, 255))
        screen.blit(back_text, (back_button_rect.x + 20, back_button_rect.y + 10))

        # --- Title ---
        title = title_font.render("Search Page", True, (255, 255, 255))
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 80))

        # --- If no voice command yet, show "Listening..." ---
        if listening:
            listen_text = small_font.render("Listening for voice command...", True, (200, 200, 200))
            screen.blit(listen_text, (screen.get_width() // 2 - listen_text.get_width() // 2, 140))

        # --- Voice command check ---
        if voice_command_queue and not voice_command_queue.empty():
            command = voice_command_queue.get().lower()
            latest_voice_command = command
            listening = False

            if command in ("back", "home", "go back", "exit"):
                return
            elif command.startswith("play "):
                title_text = command[5:].strip().lower()
                for video in matched_videos:
                    if video["title"].lower() == title_text:
                        play_video(screen, video["path"], bg_image, voice_command_queue)
                        break
            else:
                matched_videos = search_videos(command)

        # --- Show search results if available ---
        spacing_x, spacing_y = 250, 220
        col_count = screen.get_width() // spacing_x
        start_y = 180
        for i, video in enumerate(matched_videos):
            thumbnail = generate_thumbnail(video["path"])
            if not thumbnail:
                continue
            x = (i % col_count) * spacing_x + 25
            y = (i // col_count) * spacing_y + start_y
            rect = pygame.Rect(x, y, 200, 120)
            screen.blit(thumbnail, rect)
            screen.blit(font.render(video["title"], True, (255, 255, 255)), (x, y + 125))
            screen.blit(font.render(video["description"], True, (255, 255, 255)), (x, y + 150))
            thumb_rects.append((rect, video["path"]))

        render_voice_command(screen, latest_voice_command)
        pygame.display.flip()
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return
                for rect, video_path in thumb_rects:
                    if rect.collidepoint(event.pos):
                        play_video(screen, video_path, bg_image, voice_command_queue)
