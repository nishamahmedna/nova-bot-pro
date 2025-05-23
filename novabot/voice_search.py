# voice_search.py
import os
import json

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

def search_videos_by_keyword(keyword):
    results = []
    keyword = keyword.lower()
    for category, path in PAGES.items():
        metadata_path = os.path.join(path, "metadata.json")
        if not os.path.exists(metadata_path):
            continue
        with open(metadata_path, "r") as f:
            try:
                videos = json.load(f)
                for video in videos:
                    if keyword in video["title"].lower() or keyword in video["description"].lower():
                        results.append({
                            "file": os.path.join(path, video["file"]),
                            "title": video["title"],
                            "description": video["description"],
                            "category": category
                        })
            except json.JSONDecodeError:
                continue
    return results
