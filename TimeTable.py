from datetime import datetime
import pyttsx3
from notifypy import notify

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")    

FiveTo6 = '''
In This Time , 
You Have To Get Up & Listen Somethintg Positive .
5:00 Am To 6:00 Am 
Thanks.
'''

SixTo9 = '''
In This Time , 
You Have To Code .
6:00 Am To 9:00 Am .
Thanks .
'''

NineTo10 = '''
In This Time ,
You have To get Ready .
9:00 Am To 10:00 Am .
Thanks .
'''

TenTo11 = '''
In This Time ,
You have to go to school.
10:00 Am To 11:00 Am .
Thanks .
'''

ElevenTo15 = '''
In This Time ,
Study In School.
11:00 Am To 3:00 Pm .
Thanks .
'''

FifteenTo17 = '''
In This Time ,
You Have Tution .
3:00 Pm To 5:00 Pm .
Thanks .
'''

SeventeenTo22 = '''
In This Time ,
You Have Tution .
5:00 Pm To 10:00 Pm .
Thanks .
'''

TwentyTwoTo00 = '''
In This Time ,
You Have To Study .
10:00 Pm To 12:00 Pm .
'''

def Time():

    hourl = int(datetime.now().strftime("%I:%M:%S %p"))

    if hourl>=5 and hourl<6:
        Speak(FiveTo6)
        return FiveTo6
        
    elif hourl>=6 and hourl<9:
        Speak(SixTo9)
        return SixTo9

    elif hourl>=9 and hourl<10:
        Speak(NineTo10)
        return NineTo10

    elif hourl>=10 and hourl<11:
        Speak(TenTo11)
        return TenTo11

    elif hourl>=11 and hourl<15:
        Speak(ElevenTo15)
        return ElevenTo15

    elif hourl>=15 and hourl<17:
        Speak(FifteenTo17)
        return FifteenTo17

    elif hourl>=17 and hourl<22:
        Speak(SeventeenTo22) 
        return SeventeenTo22

    elif hourl>=22 and hourl<12:
        Speak(TwentyTwoTo00)
        return TwentyTwoTo00       
        
    else:
        Speak("In This Time , You Have To Sleep ")

        return '''In This Time , You Have To Sleep .'''    

def timeTable():

    Speak("Checking....")

    value = Time()

    Noti = notify()

    Noti.title = "TimeTable"

    Noti.message = str(value)

    Noti.send()

    Speak("AnyThing Else Sir ??")

timeTable()    