import pyttsx3 
import speech_recognition as sr
import datetime
import pywhatkit
import pyjokes
import wikipedia
import webbrowser
import os
import cv2
import random
import smtplib
import requests
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


Master = ["Sir", "Aryan", "Deepam", "Adarsh"]


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!"+ Master[0])

    elif hour>=12 and hour<18:
        speak("Good Afternoon!"+ Master[0])

    else:
        speak("Good Evening!"+ Master[0])

    speak(f"I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        print(query)
        if 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)

        elif 'search' in query:
            search = query.replace('search', '')
            speak('searching' + search)
            pywhatkit.search(search)

        elif 'information' in query:
            search = query.replace('information', '')
            speak('searching')
            pywhatkit.info(search,lines=4)

        elif 'ip address' in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open notepad' in query:
            codePath = 'C:\\Windows\\system32\\notepad.exe'
            speak('opening Notepad')
            os.startfile(codePath)

        elif 'open youtube' in query:
            url = 'youtube.com'

            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query:
            url = 'google.com'
            speak('what should i search on google')
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'sad' in query:
            speak("don't be sad you are one of the best guy whom i like most")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'open stackoverflow' in query:
            url = 'stackoverflow.com'
            webbrowser.get(chrome_path).open(url)

        elif 'close notepad' in query:
            speak('ok sir, closing notepad')
            os.system("taskkill /f /im notepad.exe")

        elif 'sing a song' in query:
            music_dir = 'C:\\Users\\kumar satwik kaushal\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = 'C:\\Users\\kumar satwik kaushal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            speak('opening vs code')
            os.startfile(codePath)

        elif 'open command prompt' in query:
            speak('opening cmd')
            os.system('start cmd')

        elif 'girlfriend' in query:
            speak("Sorry, i have a boyfriend, but i will add you in list of best friends")

        elif 'how are you' in query:
            speak("i am good sir, thanks for asking ,i hope you will be great too")

        elif 'who are you' in query:
            speak("I am Jarvis Sir. Please tell me how may I help you")

        elif 'thank you' in query:
            speak("Its my pleasure sir. i am here for you")

        elif 'send message on whatsapp' in query:
            try:
                speak('what should i send sir')
                str = takeCommand().lower()
                pywhatkit.sendwhatmsg("+91xxxxxxxxxx",str,22, 28)
                print("Successfully Sent!")

            except:
                print("An Unexpected Error!")

        elif 'email to abc' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "abc@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Master. I am not able to send this email")
        elif 'no thanks' in query:
            speak('Thanks for using me sir, bye bye have a great day')
            sys.exit()

