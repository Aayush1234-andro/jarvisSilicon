from logging import PlaceHolder
from urllib.parse import uses_relative
from geopy import location
import pywhatkit
import wikipedia
from pywikihow import search_wikihow
import os
import webbrowser as web
import pyttsx3
from time import sleep
import requests

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)