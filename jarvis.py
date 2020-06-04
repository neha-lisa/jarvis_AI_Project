import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import googlesearch
# import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morining dear Neha")
    elif hour>=12 and hour<18:
        speak("Good Afternoon lady neha")
    else:
        speak("Good evening")

    speak("I am jarvis madam neha Please tell how may help you")

def takeCommand():
    '''
        It takes micro phone input from user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query

# def sentEmail(to, content):
#     server = smtplib.SMTP('smtp.gamil.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com','your password')
#     server.sendmail('youremail@gmail.com',to,content)
#     server.close()

if __name__ =="__main__": 
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for exceuting tasks
        if 'wikipedia' in query:
            speak('Seaching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        # elif 'play music' in query:
        #     music_dir = 'D://'
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam ,the time is{strtime}") 
        elif 'open vscode' in query:
            codepath = "D:\Microsoft VS Code\Code.exe"
            os.startfile(codepath)
        elif 'open chrome' in query:
            webbrowser.open("yourchromepath") #please copy the chrome browser path from pc saved location
        # elif 'sent email' in query:
        #     try:
        #         speak("what should I say?")
        #         content = takeCommand()
        #         to = "Youremail@gmail.com" # please write your favourite email
        #         sentEmail(to,content)
        #         speak("email has been sent !")
        #     except Exception as e:
        #         print(e)
        #         speak("sorry neha . I am not abhle to send this email")
        elif 'who are you' in query:
            speak("I am Jarvis an AI project developed by my creator madam neha and I want love")
        elif 'who created you' in query:
            speak("I was created on 03 june 2020 and my creator is madam neha she is a 2nd year bca pursing BCA a professional degree from Institute of Engineering and Management(IEM)")
        elif 'what is your name' in query:
            speak("I am jarvis")
        elif 'search' in query:
            query_s = takeCommand()
            for j in search (query_s,tld="co.in",num=10,stop=10,pause=2):
                speak(j)
                print(j)
        elif 'stop' in query:
            exit()   


     
    