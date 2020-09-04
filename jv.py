#source for this project is https://www.youtube.com/watch?v=Lp9Ftuq2sVI


import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import smtplib

#webbrowser.get('windows-default').open('http://www.google.com')
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito' # it gets response to open in incognito mode.



engine = pyttsx3.init('sapi5')  #refer to microsoft for sapi5
voices = engine.getProperty('voices')
#print(voices) # it gives the voices that are in machine i.e, one male and one female.
#print(voices[1].id) # [0] refers to male and [1] refers to female.
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!!!")
    else:
        speak("Good evening!!!!")
    speak("I am Jarvis. Please tell me how may i help you")

def takeCommand():
    #it takes microphone input from the user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold =1
        audio =r.listen(source)
    try:
         print("Recognizing....")
         query  = r.recognize_google(audio,language='en-in')
         print(f"User said: {query}\n")

    except Exception as e:
         print(e)

         print("Say that again please ...... ")
         return "None"
    return  query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()



if __name__ == '__main__':
    #speak("happy vinayaka chaturthi")
    wishMe()
    while True:
        query  = takeCommand().lower()
        #logic for executing tasks
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            #trying to open in icognito mode.

            webbrowser.get(chrome_path).open_new('https://www.youtube.com')
            #webbrowser.open("https://www.youtube.com") # use full url it opens in chrome instead of internet explorer.
        elif 'open google' in query:
            # trying to open in icognito mode.
            #chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
            webbrowser.get(chrome_path).open_new('https://www.google.com')

        elif 'open stack overflow' in query:
            webbrowser.get(chrome_path).open_new('https://www.stackoverflow.com')

        elif 'play music' in query:
            music_dir='C:\\Users\\Harsha\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            #use random function so that it selects music in random order.
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strtTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtTime}")

        elif 'open code' in query:
            codePath= "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.2.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            #keep a dictionary which consists of names as keys and mailaddress as values and select them if there are any.
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "usermailaddress@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!!")
            except Exception as e:
                print(e)
                speak("sorry i am not able to send mail")

        elif 'quit' in query:
             speak("Have a nice day !!!!")
             quit()

