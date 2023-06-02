#imported all libraries required
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import wikipedia
import pyjokes
import pyaudio
import requests
from bs4 import BeautifulSoup

#accpeting the input as voice and 
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)





#function for the text to talk by the assistant
def talk(text):
    engine.say(text)
    engine.runAndWait()
    
#function to recognise the voice said by user
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening")
            talk("arey paaji bolo ji")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "gautham" in command:
                command=command.replace("gautham",'')
                talk(command)
            
    except:
        pass
    return command
    
#function for all the task to be performed
def run_gautham():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M%p')
        hour=datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            talk('Good moring')
        elif hour >=12 and hour <18:
            talk('Good Afternoon')
        else:
            talk('Good evening')
        print(time)
        talk('current time is'+ time)
    elif "search" in command:
        person=command.replace("search","")
        info=wikipedia.summary(person,3)
        print(info)
        talk(info)
    elif "date" in command:
        talk("sorry")
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif 'spotify' in command:
        talk('Opening Spotify..')
        webbrowser.open('open.spotify.com')
    elif 'youtube' in command:
        talk('Opening youtube..')
        webbrowser.open('open.youtube.com')
   
    else:
        talk("please say the command")
while True:  
    run_gautham()




