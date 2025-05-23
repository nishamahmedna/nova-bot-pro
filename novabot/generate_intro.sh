#!/bin/bash

# Step 1: Generate robotic intro sound using SoX
sox -n -r 44100 -c 2 robo_intro.wav synth 0.5 sine 440 vol 0.5 \
    synth 0.3 sine 880 vol 0.4 \
    synth 0.3 sine 220 vol 0.3 \
    pad 0.2 0.1

# Step 2: Generate TTS voice using espeak
espeak "Welcome to NovaBot" -w tts_welcome.wav

# Step 3: Ensure both files have the same sample rate and channels
sox robo_intro.wav -r 44100 -c 2 robo_intro_fixed.wav
sox tts_welcome.wav -r 44100 -c 2 tts_welcome_fixed.wav

# Step 4: Combine both into one file
sox robo_intro_fixed.wav tts_welcome_fixed.wav final_intro.wav

# Clean up temporary files
rm robo_intro_fixed.wav tts_welcome_fixed.wav

echo "✅ Final intro sound created: final_intro.wav"
