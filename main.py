import datetime
import webbrowser
import openai
from config import apikey

import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("SAPI.spVoice")

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for prompt - {prompt}\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": ""
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])

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
    say("Desktop AI Buddy")

    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"], ["music", "https://music.youtube.com"]]

        for site in sites:
            if (f"Open {site[0]}").lower() in query.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")
            print(f"Sir the time is {strfTime}")

        if "exit".lower() in query.lower():
            say("Exiting the Program sir")
            exit()

        if "Using AI".lower() in query.lower():
            ai(query)
