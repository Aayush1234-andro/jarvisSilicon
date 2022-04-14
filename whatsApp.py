from datetime import date, datetime
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
import webbrowser as web

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[2].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def WhatsappMsg(name,message):
     
    startfile("C:\\Users\\91916\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=195, y=115)

    sleep(1)

    write(name)

    sleep(0.5)

    click(x=188, y=249)

    sleep(0.5)

    click(x=571, y=690)

    sleep(0.5)

    write(message)

    press('enter')

def WhatsappCall(name):

    startfile("C:\\Users\\91916\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=195, y=115)

    sleep(1)

    write(name)

    sleep(1)

    click(x=188, y=249)

    sleep(1)

    click(x=571, y=690)

    sleep(1)

    click(x=1198, y=63)

def WhatsappChat(name):

    startfile("C:\\Users\\91916\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=195, y=115)

    sleep(1)

    write(name)

    sleep(1)

    click(x=188, y=249)

    sleep(1)

    click(x=571, y=690)

    sleep(1)