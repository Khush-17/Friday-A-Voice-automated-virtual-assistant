🎙️ FRIDAY – Python Voice Assistant

FRIDAY is a Python-based voice assistant inspired by popular virtual assistants like Alexa and Google Assistant.
It listens for a wake word, understands voice commands, performs everyday tasks, fetches real-time information, and responds using text-to-speech.

🚀 Features

🎤 Voice input using microphone

🗣️ Wake-word detection ("Friday")

🔊 Text-to-speech using gTTS + Pygame

🌐 Open popular websites (Google, YouTube, Facebook, LinkedIn)

🎵 Play music using a custom music library

📰 Fetch and read live news headlines using NewsAPI

🤖 AI-powered responses using OpenAI API

🧠 Fallback to AI when command is not predefined

🛠️ Technologies Used

Python

speech_recognition

gTTS

pygame

pyttsx3 (legacy / optional)

requests

webbrowser

OpenAI API

NewsAPI

📂 Project Structure
FRIDAY/
│── main.py
│── musicLibrary.py
│── README.md

🧪 How It Works

FRIDAY continuously listens for the wake word

On detecting "Friday", it enters command mode

Predefined commands are executed locally

Unknown commands are sent to OpenAI for intelligent replies

All responses are spoken using gTTS and Pygame

⚙️ Installation & Setup
1️⃣ Install Dependencies
pip install speechrecognition gtts pygame pyttsx3 requests openai pyaudio

2️⃣ Microphone Setup

Ensure microphone access is enabled

Internet connection required for speech recognition and AI

🔐 Environment Variables (IMPORTANT)

❌ Never hardcode API keys in source code

Set environment variables instead:

Windows (PowerShell)
setx OPENAI_API_KEY "your_openai_api_key"
setx NEWS_API_KEY "your_newsapi_key"

Linux / macOS
export OPENAI_API_KEY="your_openai_api_key"
export NEWS_API_KEY="your_newsapi_key"


Then access in Python:

import os
api_key = os.getenv("OPENAI_API_KEY")
newsapi = os.getenv("NEWS_API_KEY")

📌 Supported Voice Commands
Command	Action
"Friday"	Wake the assistant
"Open Google"	Opens Google
"Open YouTube"	Opens YouTube
"Open Facebook"	Opens Facebook
"Play <song>"	Plays a song from library
"News"	Reads top news headlines
Any other query	AI-generated response
⚠️ Limitations

Requires internet connection

OpenAI API usage depends on available quota

Wake-word detection is basic and rule-based

Audio playback depends on system drivers

🚧 Future Improvements

Offline speech recognition (Vosk)

Improved wake-word detection

Multithreading for smoother audio

GUI interface

Command learning and personalization

👨‍💻 Author

Khush Paliwal
Computer Science Student
Interested in Python, automation, and voice-based applications

⭐ Acknowledgements

Inspired by Alexa, Google Assistant, and the concept of virtual AI assistants.

🚨 Security Warning

Before pushing to GitHub:

Remove all API keys from code

Use environment variables

Rotate keys if already exposed

🟢 Final Notes

This project is suitable for:

College mini-projects

Python portfolios

Resume and interviews

Learning APIs and automation
