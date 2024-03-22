import os

from main import say

dictapp = {"commandprompt": "cmd", "paint": "paint", "word": "winword", "excel": "excel", "chrome": "chrome", "vscode": "code", "powerpoint": "powerpnt"}

def openapp(query):
    keys = list(dictapp.keys())
    for app in keys:
        if app in query:
            say(f"Opening {dictapp[app]}, Sir")
            os.system(f"start {dictapp[app]}")

def closeapp(query):
    keys = list(dictapp.keys())
    for app in keys:
        if app in query:
            say(f"Closing {dictapp[app]}, Sir")
            os.system(f"taskkill /f /im {dictapp[app]}.exe")