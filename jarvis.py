from io import open_code
from re import L, LOCALE, S
import re
from typing import DefaultDict
import pyttsx3
from pyttsx3.engine import Engine
from pywhatkit import main
import pywhatkit
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import requests 
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import pyjokes
import pyautogui as gui
import psutil
import speedtest
from playsound import playsound
import keyboard
import time
from pytube import YouTube
from googletrans import Translator
from pywikihow import search_wikihow
import PyPDF2
from requests import get
from bs4 import BeautifulSoup
from pytube import YouTube
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import Tk
import wolframalpha
from notifypy import notify
from PyDictionary import PyDictionary as Dict
import wikipedia as googleScrap
from chatBot import Chatterbot
from pytube import YouTube
from pyautogui import click
from pyautogui import hotkey
import pyperclip
from time import sleep
from nasa import NasaNews
from math import trunc
from os import link, startfile
import os
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import pyttsx3
import speech_recognition as sr
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#Text To Speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Speech To Text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")   
        query = r.recognize_google(audio, language='en-in')
        print(f"IVO Said: {query}") 
    except Exception as e:
        print("Sorry Sir, Can You Repeat That Again?")
        return "none"
    return query

def TakeHindi():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)

    try:
        print("Recognizing.....")
        query = command.recognize_google(audio,language='hi')
        print(f"You Said : {query}")

    except:
        return "none"

    return query    

#To Wish

def Tran():
    speak("Tell Me The Line!")
    line = TakeHindi()
    traslate = Translator()
    result = traslate.translate(line)
    Text = result.text
    speak(Text)

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir")
        print("Good Morning Sir")
        speak("it is")
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        speak(time)
        print(time)    

    elif hour>12 and hour <4:
        speak("Good Afternoon Sir")
        print("Good Afternoon Sir")
        speak("it is")
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        speak(time)
        print(time)    

    else:
        speak("Good Evening Sir") 
        print("Good Evening Sir ")
        speak("it is")
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        speak(time)
        print(time)    
       
    speak("I am JARVIS, Please Tell me How Can I help You?")
    print("I am JARVIS, Please Tell me How Can I help You?")





def TaskExecution():
    wish()

    while True:

        query = takecommand().lower()
        
        #Logic Building For Task

        if 'open notepad' in query:
            npath = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(npath)
            speak("Opening NotePad Sir")
            print("Opening NotePad Sir")

        elif 'close notepad' in query:
            speak("Sure Sir Closing Notepad")
            os.system("taskkill / f/ im notepad.exe")    

        elif 'open minecraft' in query:
            mpath = 'C:\\Users\\91916\\AppData\\Roaming\\.minecraft\\TLauncher-Beta.exe'   
            os.startfile(mpath)
            speak("Opening MineCraft Sir")
            print("Opening Minecraft Sir")

        elif 'open code' in query:
            os.system("C:\\Users\\91916\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            speak("Opening VS Code Sir")
            print("Opening VS Code Sir")
    

        elif 'open command prompt' in query:
            os.system("start cmd")
            speak("Opening Command Prompt Sir")
            print("Opening Command Prompt Sir")

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'play' in query:
            keyboard.press('space bar')    

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')    

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            print,speak("Opening Camera Sir")
            while True:
                ret , img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()        

        elif 'play music' in  query:
            music_dir = "C:\\jarvis Accessories\\music for jarvis"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            print,speak("Playing Music Sir")

        elif 'music on youtube' in query:
            speak("Sir What song would you lke to hear")
            music = takecommand()
            pywhatkit.playonyt(music)
            speak("Enjoy Sir")

        elif 'video on youtube' in query:
            speak("Sir What would you like to watch")
            movie = takecommand()
            pywhatkit.playonyt(movie)
            speak("Enjoy Sir")    

        if 'close this tab' in query:
            keyboard.    press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.    press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.    press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.    press_and_release('ctrl +h') 

        elif 'time table' in query:
            from TimeTable import timeTable
            timeTable()       

        elif 'home screen' in query:

            keyboard.    press_and_release('windows + m')

        elif 'minimize' in query:
    
            keyboard.    press_and_release('windows + m')
    
        elif 'show start' in query:
    
            keyboard.press('windows')
    
        elif 'open setting' in query:
    
            keyboard.    press_and_release('windows + i')
    
        elif 'open search' in query:
    
            keyboard.    press_and_release('windows + s')
    
        elif 'screen shot' in query:
    
            keyboard.    press_and_release('windows + SHIFT + s')
    
        elif 'restore windows' in  query:
    
            keyboard.    press_and_release('Windows + Shift + M')
    

        elif 'open external camera' in query:
            print,speak("Opening External Camera Sir")
            cap = cv2.VideoCapture(1)
            while True:
                ret , img = cap.read()
                cv2.imshow('extracam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()        
 
        elif 'start mathematics timer' in query:
            tpath = 'C:\\jarvis Accessories\\timer\\timer.mp4'
            os.startfile(tpath)
            print,speak("Starting Your 30 Minutes Timer Sir")
    

        elif 'IP address' in query:
            ip = get('https://api.ipify.org').text    
            speak(f"sir your IP address is {ip}")
            print(f"Sir Your IP Address is{ip}")


        elif 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M:%S %p')
            speak(time)
            print(time)  

        elif 'google scrap search' in query:
            
            query = query.replace("jarvis","")
            query = query.replace("google scrap search","")
            query = query.replace("google","")
            speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                speak(result)
                print(result)

            except:
                speak("No Speakable Data Available!")      

        elif 'open youtube'  in query:
            webbrowser.open('www.youtube.com')

        elif 'open facebook' in query:
            webbrowser.open('www.facebook.com')    

        elif 'open stackoverflow' in query:
            webbrowser.open('www.stackoverflow.com')    

        elif 'open google' in query:
            webbrowser.open('www.google.com')

        elif "calculate" in query:
             
            app_id = "54ETLT-9Y53TLHJP8"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'repeat my word' in query:
            speak("speak Sir!")
            jj = takecommand()
            speak(f"You Said : {jj}") 

        elif 'launch' in query:
            speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'www.' + name + '.com'
            webbrowser.open(web)
            speak("Done Sir!")
          

        elif 'make a search on google' in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")    

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'switch window ' in query:
            gui.press('alt')
            gui.press('tab')
            time.sleep(1)
            gui.press('alt')

        elif 'tell me today news ' in query:
            speak("Sure Sir")
            main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=fc4a68dc24d4416d9cd867b93bdb3bdd'    
            
            main_page = requests.get(main_url).json()
            articles = main_page["Articles"]
            head = []
            day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
            for ar in articles:
                head.append(ar["title"])
            for i in range (len(day)):
                speak(f"today's {day[i]} news is : {head[i]}")    

            
        elif 'take screenshot' in query:
             speak("sir please tell me the name for this screenshot file")
             name = takecommand().lower()
             speak("sir please hold the screen for a few seconds i am taking screenshot")
             img = gui.screenshot()
             img.save(f"{name}.png")
             speak("i am done sir")

        elif 'check the battery' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system has {percentage} percent battery") 
            if percentage>=75:
                speak("sir we have enough power to continue our work")
            elif percentage>=40 and percentage<75:
                speak("sir we should charge our battery")
            elif percentage>15 and percentage<=30:
                speak("sir we dont have enough power we should connect to charger")
            elif percentage<=15:
                speak("sir if you dont connect to charger system may die soon")    


        elif 'internet speed' in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second   downloading speed and {up} bit per second as uploading speed")

        elif 'i am upset' in query:
            speak("sir i am here with you")

        elif 'i am feeling very happy' in query:
            speak("its glad to know that you are happy")


        elif'shut down the system' in query:
            os.system("shutdown/s /t 5")

        elif'restart the system' in query:
            os.system("shutdown/r /t 5")

        elif'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0") 

        elif 'youtube search' in query:
          speak("OK sIR , This Is What I found For Your Search!")
          query = query.replace("jarvis","")
          query = query.replace("youtube search","")
          web = 'https://www.youtube.com/results?search_query=' + query
          webbrowser.open(web)
          speak("Done Sir!")  

        elif "translate to english" in query:
           speak("Tell Me The Line!")
           line = TakeHindi()
           traslate = Translator()
           result = traslate.translate(line)
           Text = result.text
           speak(Text)
        
        elif "translate to hindi" in query:
           speak("Tell Me The Line!")
           line = takecommand()
           traslate = Translator()
           result = traslate.translate(line)
           Text = result.text
           speak(Text)

        elif "where am i" in query:

            speak("Checking....")
            speak("Sir you are currently in block A of JVM vishnupuram situated in joshimath, uttarakhand")

        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            speak(f"Whats The Message For {Name}")
            MSG = takecommand()
            from whatsApp import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from whatsApp import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("jarvis ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            speak("With Whom ?")
            name = takecommand()
            from whatsApp import WhatsappChat
            WhatsappChat(name)
    

        elif 'how to' in query:

            max_result = 1

            how_to_func = search_wikihow(query=query,max_results=max_result)

            assert len(how_to_func) == 1

            how_to_func[0].print()

            speak(how_to_func[0].summary)

        elif "hide all files" in query or "visible for everyone" in query:
            speak("sir please tell me do you want to make this file visible or make it hide for every one")    
            condition = takecommand().lower()

            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("sir all the files in this folder are hidden")
            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir all the files in this folder are now visible for everyone")
            elif "leave it for now" in condition:
                speak("ok sir as you wish")   

        elif "temperature" in query:
            search = " joshimath"
            url = f"https://www.google.com/search?q=temperature in{search}" 
            r = requests.get(url)
            data = BeautifulSoup(r.text , "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"sir current temperature in {search} is {temp}")

            speak("Do I Have To Tell You Another Place Temperature ?")
            next = takecommand()

            if 'yes' in next:
                speak("Tell Me The Name Of tHE Place ")
                name = takecommand().lower()
                search = f"temperature in {name}"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temperature = data.find("div",class_ = "BNeawe").text
                speak(f"The Temperature in {name} is {temperature}")
    
            else:
                speak("no problem sir")

        elif 'volume up' in query:
            gui.press("volumeup")

        elif 'volume down' in query:
            gui.press("volumedown")

        elif 'volume mute' in query:
            gui.press("volumemute") 

        elif "sleep" in query:
            speak("OK sir I am Going To sleep you can call me any time")
            break  

        if 'hello' in query:
            speak("Hello Sir , I Am Jarvis .")
            speak("Your Personal AI Assistant!")
            speak("How May I Help You?")

        elif 'how are you' in query:
            speak("I Am Fine Sir!")
            speak("Whats About YOU?") 

        elif "also fine" in query or "fine" in query:
            speak("I am Happy If You are happy")    

        elif 'translator' in query:
            Tran()

        elif 'close youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'close chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'close telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'close code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'close instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'close brave' in query:
            os.system("TASKKILL /F /im Brave.exe")  

        elif 'covid cases' in query:

            from coronatracker import CoronaVirus

            speak("Which Country's Information ?")

            cccc = takecommand()

            CoronaVirus(cccc)

        elif 'download this video' in query:
            sleep(2)

            click(x=942,y=59)
        
            hotkey('ctrl','c')
        
            value = pyperclip.paste()
        
            Link = str(value) # Important 
        
            def Download(link):
        
                url = YouTube(link)
        
                video = url.streams.first()
        
                video.download('C:\\School Project\\database\\YouTube')
        
            Download(Link)
        
            speak("Done Sir , I Have Downloaded The Video .")
            speak("You Can Go And Check It Out.")
        
            os.startfile('C:\\School Project\\database\\YouTube')

        elif 'dictionary' in query:
            speak("Activating Dictionary")
            speak("Sir tell me the problem")
            prob = takecommand()

            if 'meaning' in prob:
                prob = prob.replace("what is the","")
                prob = prob.replace("jarvis","")
                prob = prob.replace("of","")
                prob = prob.replace("the meaning of", "") 
                result = dict.meaning(prob)
                speak(f"the meaning for {prob} is {result}")
                print(f"the meaning for {prob} is {result}")

            elif 'synonym' in prob:
                prob = prob.replace("what is the","")
                prob = prob.replace("jarvis","")
                prob = prob.replace("of","")
                prob = prob.replace("the synonym of", "") 
                result = dict.synonym(prob)
                speak(f"the synonym for {prob} is {result}")
                print(f"the synonym for {prob} is {result}")   

            elif 'antonym' in prob:
                prob = prob.replace("what is the","")
                prob = prob.replace("jarvis","")
                prob = prob.replace("of","")
                prob = prob.replace("the antonym of", "") 
                result = dict.antonym(prob)
                speak(f"the antonym for {prob} is {result}")
                print(f"the antonym for {prob} is {result}")       


        elif "Good Bye" in query:
            speak("Thank you for using me sir have a good day")
            sys.exit()              

        elif 'i need to code an update for my app' in query:
            webbrowser.open("https://developer.android.com/games/agde/measure")

        elif 'space news' in query:

            speak("Tell Me The Date For News Extracting Process .")

            Date = takecommand()

            from dateConverter import DateConverter

            Value = DateConverter(Date)

            NasaNews(Value)

        elif 'about' in query:
            from nasa import Summary
            query = query.replace("jarvis ","")
            query = query.replace("about ","")
            Summary(query) 

        elif 'near earth' in query:
            from nasa import Astro
            from dateConverter import DateConverter
            speak("Tell Me The Starting Date .")
            start = takecommand()
            start_date = DateConverter(takecommand)
            speak("And Tell Me The End Date .")
            end = takecommand()
            end_date = DateConverter(end)
            Astro(start_date,end_date=end_date)   

        elif 'set an alarm' in query:
            speak("tell me the time sir")
            time = input(":TYPE DOWN THE TIME HERE:")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time To Wake Up Sir!")
                    os.startfile('lol.mp3')

                elif now>time:
                    break    
                
                if 'close the alarm' in prms:
                    os.close("lol.mp3")    

        elif 'increase' in query:

            press_and_release('SHIFT + .')

        elif 'decrease' in query:

            press_and_release('SHIFT + ,')

        elif 'previous' in query:

            press_and_release('SHIFT + p')

        elif 'next' in query:

            press_and_release('SHIFT + n')
    
        elif 'search' in query:

            click(x=667, y=146)
    
            speak("What To Search Sir ?")
    
            search = takecommand()
    
            write(search)
    
            sleep(0.8)
    
            press('enter')

        if 'home screen' in query:

            press_and_release('windows + m')

        elif 'minimize' in query:

            press_and_release('windows + m')

        elif 'show start' in query:
 
            press('windows')

        elif 'open setting' in query:

            press_and_release('windows + i')

        elif 'open search' in query:

            press_and_release('windows + s')

        elif 'screen shot' in query:

            press_and_release('windows + SHIFT + s')

        elif 'restore windows' in  query:

            press_and_release('Windows + Shift + M')  
            
        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            speak("You Tell Me That" + remeber.read())      

        elif 'introduce yourself' in query:
            speak("yes sir")
            speak("hello i am jarvis A personal assistant which is created virtually by my master Aayush kumar")

        elif "Good Bye" in query:
            speak("Thank you for using me sir have a good day")
            sys.exit()  
             
        elif "play  my favourite" in query:
            os.startfile("joker.mp3")
            speak("Enjoy Sir!")    
        
    
if __name__ == "__main__":
    while True:
        #playsound('C://School Project//jarvis.mp3')
        prms = takecommand()
        if "wake up" in prms:
            TaskExecution()
        elif "Good Bye" in prms:
            speak("Thank you for using me sir have a good day")
            sys.exit()           