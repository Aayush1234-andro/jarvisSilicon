import random

Command_1 = ["hello","wake up","you there jarvis","hi there","need your help","i need you","namaste","hey","kya hal hai","kya kar rahe ho"]

Command_2 = ["bye","sleep","go and sleep","need a break","bye there","shut down","rest","help yourself","jao"]

Command_3 = ["help me","what can you do","your functions","your abilities","you should help me"]

reply_1 = ["Hello sir",
"Welcome Back Sir",
"Hi",
"Hey there",
"What's up Sir ?",
"As Usual Sir",
"Let Me Get Started",
"Good To See You Again Sir"]

reply_2 = ["Bye sir",
"See You Again Sir",
"I Will Be There For You",
"Bye Sir , If You Want To Start Me . Speak - Wake Up Jarvis .",
"Have a good day!", "It was wonderful to talk with you. I must be going ",
"It was great to talk with you. I look forward to seeing you again soon ",
"It will be great to see you again."]

reply_3 = ["Let Me Ask You First , What Can I Do For You Sir ?",
"my functions Are Written Inside Me ",
"Do You Want Me To Tell You My Functions ?",
"I Can Help You With Many Varieties Of Task ",
"I Think , You Should Give Me Command First ",
"Ohh So Funny Sir , You Knew It Already ",
"I Can Call Your Girl Friend ",
"I Can Turn The Incognito Mode On ",
"I Can Sleep Sir",
"Oh Nice Question . But Whats The Question ?",
"Thanks Me In Advance"]

def Chatterbot(Text):

    if "your abilities" in Text:
        return random.choice(reply_3) + "."

    elif 'need a break' in Text:
        return random.choice(reply_2)

    elif 'help me' in Text:
        return random.choice(reply_3) + "."

    elif 'you there jarvis' in Text:
        return random.choice(reply_1)

    elif 'shut down' in Text:
        return random.choice(reply_1)

    elif 'kya hal hai' in Text:
        return random.choice(reply_1)

    elif 'kya kar rahe ho' in Text:
        return random.choice(reply_1)

    elif 'i need you' in Text:
        return random.choice(reply_1)

    elif 'wake up' in Text:
        return random.choice(reply_1)

    elif 'hi there' in Text:
        return random.choice(reply_1)

    elif 'need your help' in Text:
        return random.choice(reply_1)

    elif 'your functions' in Text:
        return random.choice(reply_3)

    else:

        for word in Text.split():

            if word.lower() in Command_1:
                return random.choice(reply_1) + "."

            elif word.lower() in Command_2:
                return random.choice(reply_2) + "."

            elif word.lower() in Command_3:
                return random.choice(reply_3) + "."