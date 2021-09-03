import speech_recognition as sr
import wikipedia
import pyttsx3
import datetime
import webbrowser
import os
import smtplib


engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)
# print(voices[0].id)
def speak(audio):
    # it coverts text into voice 
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")


    elif hour>=12 and hour<16:
        speak("Good Afternoon")
 
    else:
        speak("Good Evening")

    speak("Iam Mac Please tell me how may i help you ")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo
    server.starttls('karan7073083447@gmail.com','your password')
    server.sendmail('karan7073083447@gmail.com',to,content)
    server.close()

if __name__=="__main__":
 # speak("karan is a good boy")
    wishMe()
    while True:
    
     query = takeCommand().lower()
    #  Logic for executing tasks based on query
     if 'wikipedia' in query:
         speak('Searching Wikipedia...')
         query = query.replace("wikipedia", " ")
         results = wikipedia.summary(query,sentences=2)
         speak("According to Wikipedia")
         speak(results)
         
     elif 'open youtube' in query:
         webbrowser.open("youtube.com")

     elif 'open google' in query:
          webbrowser.open("google.com")

     elif 'open stackoverflow' in query:
          webbrowser.open("stackoverflow.com")

     elif 'open facebook' in query:
          webbrowser.open("facebook.com")




     elif 'play music' in query:
         music_dir = 'E:\\Song\\download'
         songs = os.listdir(music_dir)
         print("songs")
         os.startfile(os.path.join(music_dir,songs[0]))


     elif 'the time' in query:
         strTime = datetime.datetime.now().strftime('%H:%M:%S')
         speak(f" sir the  time is {strTime}")

     elif 'open code' in query:
         codepath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codepath)

     elif "send email" in query:
         try:
             speak("What should I say")
             content = takeCommand()
             to = "karan7073083447@gmail.com"
             sendEmail(to,content)
             speak("Email has been sent !")
         except Exception as e:
             print(e)    
             speak("Sorry my friend karan . I am not able to send this email")