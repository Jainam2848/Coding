import speech_recognition as sr
import pyttsx3 as p

engine = p.init("sapi5")

voices = engine.getProperty("voices")
engine.connect("voices", voices[1].id)
duration = 4

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.record(source, duration=duration)
        query = ""
        try:
            print("Recognizing....")
            query = r.recognize_google(audio)
            print(f"User said : {query}")
        except Exception as e:
            speak("Say that again!")
            return "none"
    return query
#listen()

        
speak("Welcome to Aashirwad kirana store")
speak('We have following items available at the moment :')

print('We have following items available at the moment :')

items = ['Garam Masala', 'Almonds', 'Kaju', 'Chilli powder', 'Turmeric powder']

prices = [500, 650, 680, 250, 150]
customer_list = []
total_bill = 0
i = 0

while  i<len(items):
    print('1 kg price of',items[i],'is :', prices[i])
    i+=1 
 
for i in range(len(items)):
    items[i] = items[i].lower()
    
while True: 
    
    speak("What would you like to purchase ? or say exit :")
    #user_input = input('What would you like to purchase ? or press q to exit  :').lower()
    query = listen().lower()
        
    if 'exit' in query:
        break
    
    elif 'garam masala' in query or 'garam' in query :
        speak("garam masala has been added ")
        
        customer_list.append(query)
        speak("How much kilogram :")
        query1 = int(listen()) 
        
        total_bill =  total_bill + int(query1)*500
        
    elif 'almonds' in query or 'alomond' in query:
        speak("almonds have been added ")
        customer_list.append(query)
        speak("How much kilogram :")
        query1 = listen() 
        
        total_bill =  total_bill + int(query1)*650
        
    elif 'kaju' in query:
        speak("kaju has been added ")
        customer_list.append(query)
        speak("How much kilogram :")
        query1 = listen() 
        
        total_bill =  total_bill + int(query1)*680
        
    elif 'chilli powder' in query:
        speak("chilli powder has been added ")
        customer_list.append(query)
        speak("How much kilogram :")
        query1 = listen() 
        
        total_bill =  total_bill + int(query1)*250
        
    elif 'turmeric powder'in query or 'turmeric' in query:
        speak("turmeric powder has been added ")
        customer_list.append(query)
        speak("How much kilogram :")
        query1 = listen() 
        
        total_bill =  total_bill + int(query1)*150
        
    else:
        print("Please choose your item from the list.")
        
print()    
print("Your list of items is :",[customer_list])   

speak("Your list of items is :")

speak(customer_list) 
print("Your total bill is :")
  
speak("Your total bill is ")
speak(total_bill)
print(total_bill)

speak("Thank you for Shopping with us !🙏")