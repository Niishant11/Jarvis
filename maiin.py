import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from openai import OpenAI


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    clint = OpenAI(api_key="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")
    completion = clint.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open stack overflow" in c.lower():
        webbrowser.open("https://stackoverflow.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        webbrowser.open("https://news.google.com")

    else:
        # let openAi handle the command
        output = aiprocess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing... Jarvis")
    while True:
        # Initialize the recognizer
        r = sr.Recognizer()
        # Set the microphone as the source
        
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                print(f"You said: {word}")
                speak("Yes sir")
                    #listen for command
                with sr.Microphone() as source:
                    print("jarvis Active...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    print(f"You said: {command}")
                    


                    process_command(command)

            # Check for specific commands                  
        except Exception as e:
                print("Error;{0}".format(e))
                
