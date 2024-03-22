from main import say
import datetime

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        say("Good Morning, Sir")
    elif hour>=12 and hour<18:
        say("Good Afternoon, Sir")
    elif hour>=18 and hour<=24:
        say("Good Evening, Sir")
    else:
        say("Good Night, Sir")
    say("How can I help you sir")