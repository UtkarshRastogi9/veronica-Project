"""
Veronica-- Voice Based Virtual Assistant
Write the Following Commands in the terminal for running this program successfully:
pip install pyttsx3
pip install speechRecognition
pip install wikipedia
pip install pipwin
pipwin install pyaudio
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
import pywhatkit
import pyjokes
from numpy import random
from time import ctime
client  = wolframalpha.Client('XEQ3GP-G74249KTGW')

#api id
#XEQ3GP - XJ4UU2TEJA
engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def  wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Boss!...")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon Boss!...")
    else :
        speak("Good Evening Boss!...")
    # speak("My name is Veronica... ")


def takeCommand():

    # It takes microphone input from the user and returns string output.
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,3)
        print("Listening")
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in',)
        print(f"User Said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        query = takeCommand().lower()
        # return "None"
    return query


def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id ','your password')
    server.sendmail('your email address',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    speak('Boss!...,Do you want to initiate my systematic functionality?')
    choice = takeCommand().lower()

    while "yes" in choice or "sure" in choice or "of course" in choice or "yeah" in choice:
        speak(random.choice(['OK!... How May I help you ?','OK!...What can I do for you ? ']))
        query = takeCommand()
        # if query == "None":
        #     speak("Fine...Good Bye")
        #     exit()
        query = query.lower()
        #Logic for executing tasks based on the query provided by the user.
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'what is your name' in query:
            speak('My name is Veronica')
        elif "who are you" in query or "define yourself" in query:
            define = '''Hello, I am Veronica. Your personal Assistant.I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etcetra'''
            print(define)
            speak(define)
        elif 'joke' in query :
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            print(My_joke)
            speak(My_joke+"......")
        elif 'search' in query:
            speak("What do you want to search for ? ")
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak('Here is what I found for'+search)
        elif 'navigate' in query:
            speak("Tell me the location you want to navigate for ? ")
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location +'/&amp;'
            webbrowser.get().open(url)
            speak('Here is what I found for'+location)
        elif 'how are you' in query:
            ch = random.choice(["I am fine sir.",'like never before','I\'m great... ','I\'m fine . Thank you....'])
            print(ch)
            speak(ch)
        elif 'open youtube' in query:
            url = 'youtube.com '
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            speak('Opening.... Youtube')
        elif 'open google' in query:
            url = 'google.com '
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            speak('Opening.... Google')
        elif 'open stack overflow' in query:
            url = 'stackoverflow.com '
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            speak('Opening.... StackOverflow')
        elif 'play music from directory' in query:
            music_dir = "C:\\Users\\Lenovo\\Documents\\Documents-Backup\\songs"
            songs = os.listdir(music_dir)
            speak("Which one do you want me to play")
            print("Which one do you want me to play")
            print(songs)
            ch = int(takeCommand().lower())
            os.startfile(os.path.join(music_dir,songs[ch]))
        elif 'play' in query:
            song = query.replace('play','')
            speak('playing'+ song)
            pywhatkit.playonyt(song)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
            print(strTime)
            speak(f"Boss , the time right now is {strTime}")
            # print(strTime)
        elif 'open adobe illustrator' in query:
            code_path ="C:\\Users\\utkar\\Adobe Illustrator\\Adobe Illustrator 2020\\Support Files\Contents\\Windows\\Illustrator.exe"
            os.startfile(code_path)
            speak('Opening.... Adobe Illusttrator')
        elif 'open outlook' in query:
            code_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(code_path)
            speak('Opening.... Outlook')
        elif 'open powerpoint' in query:
            code_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(code_path)
            speak('Opening.... Power Point')
        elif 'open code' in query:
            code_path ="C:\\Users\\utkar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
            os.startfile(code_path)
            speak('Opening.... Virtual Studio Code')
        elif 'open pycharm' in query:
            code_path ="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.1\\bin\\pycharm64.exe"
            os.startfile(code_path)
            speak('Opening.... Pycharm')
        elif 'open spotify' in query:
            code_path ="C:\\Users\\utkar\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify"
            os.startfile(code_path)
            speak('Opening.... Spotify')
        elif 'open' in query:
            speak('What do you want to open?..')
            webpage = takeCommand()
            url =  'www.'+webpage+ '.com '
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            speak('opening....'+webpage)
        elif 'send an email' in query or 'email' in query:
            speak("OK!...")
            try:
                speak('Who is the receipient?..')
                recep = takeCommand()
                to = ""
                if recep == "myself":
                    to = 'utkarsh.19b151015@abes.ac.in'
                else:
                    speak('Type the Email address below')
                    to = input('type the email:')
                speak("What should I send?")
                content = takeCommand()

                sendEmail(to, content)
                speak("Email has been sent successfully !")
            except Exception as e:
                print(e)
                speak("Sorry I was unable to send the email... ")
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    print(results)
                    speak(results)


                except:
                    speak("You can type the query here..")
                    query = input("type your query: ")
                    res = client.query(query)
                    results = next(res.results).text
                    print(results)
                    speak(results)

            except:
                speak("could not find what you are saying, you can search on google")
                webbrowser.open('www.google.com')
        speak(random.choice(["Boss!... Do you want to continue ?","Anything else ?..","want something more !!"]))
        choice = takeCommand().lower()
        if "yes" in choice or "sure" in choice or "of course" in choice or "yeah" in choice:
            continue
        else:
            speak(random.choice(["goodbye Boss.... have a nice day","Fine...Terminating the functionality","Fine... I am going to sleep now...."]))
            exit()
