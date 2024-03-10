import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('rate')
# print(voices[1].id)
new_rate=voices - 65
engine.setProperty('rate',new_rate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
    
def wishme(query1):
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"{query1} good morning")
        
    elif hour>=12 and hour<18:
        speak(f"{query1} good afternoon")
        
    else:
        speak(f"{query1} good evening")
           
    speak("i am jarvis sir. please tell me how may i help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("1️⃣  writing  ")
        print("2️⃣  speaking ")
        y=input("choose number :  ")
        if(y=="1"):
            p=input("write your wishes : ")
        else:
            print("listening.....")
            r.pause_threshold = 1
            audio=r.listen(source)
    if(y=="1"):
        return p
    else:    
        try:
            print("recognizing....")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said:{query}\n")
            
        except Exception as e:
            print("say that again please")
            return "none"
        
        
        return query
        
if __name__=="__main__":
    # speak("jenil daayo che")
    # wishme()
    speak("please tell me yoyr name")
    query1=takecommand()
    while True:
       query=takecommand().lower()
       
       if 'wikipedia' in query:
           speak('searching wikipedia..')
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           str=f'{query1} according to wikipedia'
           speak(str)
           speak(results)
           
       elif 'youtube kholo' in query:
           webbrowser.open("youtube.com")
        
       elif 'biggboss'   in query:
           webbrowser.open("https://www.jiocinema.com/videos/bigg-boss-ott-24hrs-live/3762109")
           
       elif "tarak" or "jetho" in query:
           webbrowser.open("https://www.sonyliv.com/shows/taarak-mehta-ka-ooltah-chashmah-1700000084")
           
       elif 'open google' in query:
           webbrowser.open("google.com")

       elif 'song' in query:
           music_dir="C:\\Users\\HARDIK\\Music\\tu joothi me makkkar"
           songs=os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))
        
       elif 'ketla vagya' in query:
           strtime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(strtime)

       elif 'jenil' in query:
           speak('jenil is good men')
           
       elif 'name' in query:
           speak('maru naam alexa che')     
           
       elif 'wishme' in query:
           wishme(query1)   
           
              
        

    