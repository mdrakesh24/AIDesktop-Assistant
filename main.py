import webbrowser

import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("SAPI.spVoice")

def say(text):
    speaker.speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said:{query}")
            return query
        except Exception as e:
            return "Some Error Occured, Sorry From your Desktop Buddy"

if __name__ == '__main__':
    say("Hey Hello I am your Desktop AI Buddy")
    while True:
        print("Listening...")
        text = takeCommand()
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"]]
        if site[0] in sites:
            say("Opening Youtube Sir...")
            webbrowser.open(site[1])
