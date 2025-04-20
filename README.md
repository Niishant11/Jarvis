# Jarvis

# 🤖 Jarvis – Voice-Activated AI Assistant

**Jarvis** is a smart, voice-controlled virtual assistant built using Python. It can recognize voice commands, respond verbally, perform web automation, fetch news, play music, and answer queries using OpenAI's GPT model — just like Alexa or Google Assistant, but customized!

---

## 🎯 Features

- 🎙️ **Voice Activation with Wake Word** – Listens for the word "Jarvis" before activating.
- 🧠 **AI Chat Integration** – Uses OpenAI's GPT-3.5 to generate intelligent, conversational responses.
- 🌐 **Web Automation** – Opens websites like Google, YouTube, LinkedIn, etc., on command.
- 📰 **Live News Headlines** – Fetches and reads out the latest news using NewsAPI.
- 🎵 **Music Playback** – Plays songs from a custom music library via web links.
- 🔊 **Speech Output** – Speaks responses using `gTTS` and `pygame`.

---

## 🛠️ Tech Stack

| Technology        | Usage                             |
|-------------------|------------------------------------|
| Python            | Core Programming Language          |
| speech_recognition | Voice input and processing         |
| gTTS + pygame     | Text-to-speech output              |
| OpenAI API        | AI response generation (GPT-3.5)   |
| requests          | Fetching news via News API         |
| webbrowser        | Opening web pages                  |

---

## 🧠 AI Prompt Example

The assistant is prompted as:
> "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."

---

## 🚀 Getting Started

### 🔧 Prerequisites
Install the required Python libraries:
```bash
pip install speechrecognition gTTS pygame requests openai
