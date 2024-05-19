import os
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import requests
import bs4
import datetime
import pyautogui
import keyboard
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")   
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r = sr.Recognizer()  # Create an instance of Recognizer
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
        
    try:
        print("Understanding....")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query    

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok Sir, You can me call anytime")
                    break 
                
                elif "Hello" in query:
                    speak("Hello Sir, How are you ?")
                elif "I am fine" in query:
                    speak("That's Great, Sir")
                elif "How are you" in query:
                    speak("Perfect, Sir")
                elif "Thank You" in query:
                    speak("You are Welcome, Sir")
                
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) #choose any number of songs
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open('https://www.youtube.com/watch?v=gzf7zkOVXmg') 
                
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                        pyautogui.press("k")
                        speak("video played")
                elif "mute" in query:
                        pyautogui.press("m")
                        speak("video muted")

                elif "volume up" in query:
                        from keyboard import volumeup
                        speak("Turning volume up,sir")
                        volumeup()
                elif "volume down" in query:
                        from keyboard import volumedown
                        speak("Turning volume down, sir")
                        volumedown()

                        
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                            
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query) 
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)   
                    
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()   
                    
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                    
                elif "temperature" in query:
                    search = "temperature"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = bs4.BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    
                elif "weather" in query:
                    search = "temperature"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = bs4.BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                
                elif "set an alarm" in query:
                        print("input time example:- 10 and 10 and 10")
                        speak("Set the time")
                        a = input("Please tell the time :- ")
                        alarm(a)
                        speak("Done,sir")
                        
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Ok Sir, Going to sleep")
                    exit()
                    
                elif "note that" in query:
                    rememberMessage = query.replace("note that","")
                    rememberMessage = query.replace("va","")
                    speak("You told me to "+rememberMessage)
                    note = open("note.txt","a")
                    note.write(rememberMessage)
                    note.close()
                elif "what do you noted" in query:
                    note = open("note.txt","r")
                    speak("You told me to " + note.read())
                
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                elif shutdown == "no":
                    break
                pass
            