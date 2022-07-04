import sys
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id)

engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please ...")
        return "none"
    return query

# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xnetking@gmail.com', '@Manvi1539')
    server.sendmail('xnetking@gmail.com', to, content)
    server.close()

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 16:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis please tell me, how can i help you")


if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        # logic building for task

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open python" in query:
            npath = "C:\\Python\\python.exe"
            os.startfile(npath)

        elif "chrome" in query:
            npath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "play music" in query:
            music_dir = "C:\\Users\\HP\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open google" in query:
            speak("Sir, What should I search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send whatsapp" in query:
            kit.sendwhatmsg("+918005395425", "this is test message", 6, 25)

        elif "play songs on youtube" in query:
            kit.playonyt("see you again")

        elif "email to ak" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "imaksinghrajpoot@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to ak")
            except Exception as e:
                print(e)
                speak("I'm sorry. I am unable to send this email.")

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        speak("Sir, do you have any other work")
