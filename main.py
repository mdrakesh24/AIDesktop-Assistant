import datetime
import webbrowser
import openai
import speech_recognition as sr
import win32com.client
import requests
from bs4 import BeautifulSoup
from apikey import apikey


speaker = win32com.client.Dispatch("SAPI.spVoice")

def ai(prompt):
    openai.api_key = apikey
    response = openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": ""}
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(["choices"][0]["text"])
    return response["choices"][0]["text"]


def say(text):
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError:
        return "Sorry, I couldn't reach the speech recognition service."





if __name__ == '__main__':
    say("Hello Sir, I am Your Desktop Assistant")
    say("How can I assist you sir")

    while True:
        query = takeCommand().lower()

        if "open youtube" in query:
            webbrowser.open("https://youtube.com")
            say("Opening YouTube, Sir.")

        elif "open wikipedia" in query:
            webbrowser.open("https://wikipedia.org")
            say("Opening Wikipedia, Sir.")

        elif "open google" in query:
            webbrowser.open("https://google.com")
            say("Opening Google, Sir.")

        elif "play music" in query:
            webbrowser.open("https://music.youtube.com")
            say("Playing music on YouTube Music, Sir.")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strTime}")

        elif "temperature" in query:
            url = f"https://www.google.com/search?q={query}"
            # webbrowser.open(url)
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            say(f"current {query} is {temp}")

        elif "open app" in query:
            from openapp import openapp
            openapp(query)

        elif "close app" in query:
            from openapp import closeapp
            closeapp(query)

        elif "wake up" in query:
            from greet import greetMe
            greetMe()

        elif "using ai" in query:
            ai_response = ai(prompt=query)
            print(ai_response)

        elif "exit" in query:
            say("Exiting the Program sir")
            exit()

