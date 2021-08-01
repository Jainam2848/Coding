import speech_recognition as sr
import pyttsx3 as p
import os
from PIL import Image
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import sys
import time

engine = p.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 1
        audio = r.record(source, duration=4)
        query = ""
              
        try:
            print("Recognizing....")
            query = r.recognize_google(audio)
            print(f"User said : {query}")
            
        except:
            return 'none'
                     
    return query.lower()

def sum(a,b):
    return a+b

print("Welcome sir. I am Your virtual Assistant")
speak("Welcome sir. I am Your virtual Assistant")
print("How may i help you ?")
speak("How may i help you ?")

valid_image = [".jpg"]

def Assistant():
    query = listen()
    
    if "photos" in query:
        path1 = "C://Users//lenovo B2IN//Pictures//Screenshots"
        lst = os.listdir(path1)    
        print(lst)

        #will watch all photos in screenshot directory
        for file in lst:
            
            #extracting extension 
            ext = os.path.splitext(file)[1]
            print(ext)
            
            if ext.lower()==".png":
                im = Image.open(file)    
                im.show()
    elif  "youtube" in query:
        speak('opening' + query.replace('open', ""))
         #replacing word open with empty string in user input
        webbrowser.open("youtube.com")
       
        
    elif "google" in query:
        speak('opening' + query.replace('open', ""))
        webbrowser.open("google.com")
    
    elif "gmail" in query or "email" in query or "emails" in query:
        speak('opening gmail')
        webbrowser.open("gmail.com")
        
    elif "notepad" in query:
        speak('opening' + query.replace('open', ""))
        n_path = 'C:\\WINDOWS\\system32\\notepad.exe'
        os.startfile(n_path)
        
    elif "command prompt"  in query:
        speak('opening' + query.replace('open', ""))
        os.system("start cmd")
       
    elif "play" in query:
        
        #replacing word play with empty string in user input
        query = query.replace('play', "") 
        speak('playing' + query)
        pywhatkit.playonyt(query)
        time.sleep(15)
        
    elif "wikipedia" in query or 'search' in query:
        speak("Searching on wikipedia")
        info = wikipedia.summary(query, sentences = 1)
        print(info)
        speak(info)
    
    elif "joke" in query:
        speak("Here's is the joke !")
        Joke = pyjokes.get_joke()
        print(Joke)
        speak(Joke)     
     
    elif 'add' in query:
        speak("What is the first number ?")
        a = int(listen())
        speak("What is the second number ?")
        b = int(listen())
        c = sum(a, b)
        speak("Answer is :")
        speak(c)
        print(c)
        
    elif "no thanks" in query or "no" :
        speak("Thank you sir for using me !")
        sys.exit()
    
    time.sleep(8)
    
    speak("Do you have anyother work sir ?")
        
while True:
    Assistant()
      