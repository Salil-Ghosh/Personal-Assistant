import pyttsx3
import datetime
import speech_recognition as re
import webbrowser
import wikipedia
import os
import random
import time




engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("good morning sir.")
        speak("hopefully you take breakfast at proper time")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir.")
        speak("hopefully you take lunch at proper time.")
    else:
        speak("good evening sir")
    speak("I am Ve.")
    speak("My Father Is sholil.")
    speak("tell me what can i do for you?")


def takecomand():
    r=re.Recognizer()
    with re.Microphone() as source:
        print("listening sir...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing sir...")
        query=r.recognize_google(audio,language="en-in")
        print(f"You Say:{query}")
    except:
        print("Can not Recognize ")
        # speak("please Say Again")
        return "none"
    return query



if __name__ == "__main__":
    wishme()
    while True:
        query=takecomand().lower()
        if "wikipedia" in query:
            speak("Searching in Wikipedia..")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak("according to wikipedia")
            speak(result)
        elif "open google" in query:
            speak("ok sir")
            webbrowser.open("google.com")
        elif "open youtube" in query:
            speak("obviously Dear sir")
            webbrowser.open("youtube.com")
        elif "open facebook" in query:
            speak("yepp")
            webbrowser.open("facebook.com")
        elif "open fitgirl" in query:
            speak("Piracy Is Crime")
            speak("but you are my boss")
            speak("i can do anything for you")
            webbrowser.open("https://fitgirl-repacks.site/.com")
        elif "music" in query:
            n=random.randint(0,4)
            mdir="D:\\Songs"
            songs=os.listdir(mdir)
            os.startfile(os.path.join(mdir,songs[n]))
        elif "single" in query:
            speak("i am happily single")
            speak("my father is very angry person")
            speak("He will kill me")
            speak("if i love someone")
        elif "bhe" in query:
            speak("yes sir")
        elif "my friends" in query:
            speak("Gopal")
            speak("Santanu")
            speak("soumya")
            speak("rudra")
            speak("tamal")
            speak("Amor")
            speak("and many more")
            speak("you have sooo many friends.")
        elif "dad" in query:
            speak("My Dad IS")
            speak("Sholil Kumar Ghosh")
            speak("he is very Nice")
            speak("And Kind Hearted Person")
            speak("He Always Wants Love")
            speak("But My Mom" )
            speak("Never GIve Him")
            speak("Love")
        elif "mom" in query:
            speak("My father Will Kill me")
            speak("I can't tell")
        elif "das" in query:
            speak("oooo  soumo")
            speak("I am His Srodha")
            speak("he is my crush")
            speak("i love him so much")
            speak("oh no, please\'")
            speak("don't tell my father")
        elif "yourself" in query:
            speak("i am ve")
            speak("Daughter Of Sholil")
            speak("i am an A I")
            speak("i born in")
            speak("nineteenth september")
            speak("two thousand twenty")
        elif "great" in query:
            speak("Hi")
            speak("Rudra")
            speak("how")
            speak("are you")
            speak("laora")
        elif "birthday" in query:
            os.startfile("D:\\Download\\Tamal.jpg")
            time.sleep(1)
            speak("uff")
            speak("Sorry")
            speak("wrong image")
            os.startfile("D:\\Download\\Souhardya.jpg")
            speak("This Is My Motu")
            speak("Happpy Birthday  My Motu")
            # speak("My Motu")
            speak("love You")
            speak("Many Many Happy Returns of the day")
            
            # speak("of the day")
            
        elif "sleep" in query:
            speak("oh nooooo!")
            speak("what can i do")
            speak("My father Gonna Kill me ")
            speak("bye sir")
            exit()
            

