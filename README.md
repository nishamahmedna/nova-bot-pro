# NovaBot Pro

NovaBot Pro is a voice-controlled AI interface that allows users to explore all past data, videos, tutorials, and news related to a company or organization. Designed as a smart internal showcase tool, it uses semantic voice search to match user queries with relevant visual content, offering an engaging, hands-free experience.

## 🧠 Features

- 🎙️ Voice-controlled interface with real-time speech recognition
- 🔍 Semantic search to match user queries with internal video/image/text datasets
- 🎥 Displays company project demos, news, and documentation interactively
- 🤖 Spoken responses for accessibility and enhanced engagement

## 🧰 Tech Stack

- Python, Vosk (Offline Speech Recognition)
- OpenRouter / Gemini / ChatGPT APIs for semantic NLP
- JSON metadata for media search and retrieval
- Pygame UI (or display interface with video + voice)
- ffpyplayer for audio/video playback

## 🧠 How It Works

1. User gives a voice command (e.g., “Show me tutorials on AI arm control”)
2. System performs a semantic search across tagged media
3. Matched items are shown and played back
4. NovaBot speaks the result or description aloud

## 📄 Use Case

Ideal for:
- Company booths/demos
- Internal documentation exploration
- Smart info kiosk at expos

## 🚀 Getting Started

```bash
pip install -r requirements.txt
python main.py
