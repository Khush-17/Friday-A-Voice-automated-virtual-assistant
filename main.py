import speech_recognition as sr  #need to install module, pip intall
import webbrowser  #no need to inmstall this module, cuz inbuilt
#also installed pyaudio setuptools sphynx googleaudio
import pyttsx3 #for converting text to speech
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS  #google tetxt to speech
import pygame  #to use gtts
import time
import os



recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # normal speaking speed
engine.setProperty("volume", 1.0)
newsapi = "62ba2fcb305341b296bc866bfdbcab12"



def speak_old(text):   #will speak through this function
    engine.say(text)  #microsoft inbuilt function to speak
    engine.runAndWait()
    
    
    
    
def speak(text):   #new method for speech, used with py game
    tts = gTTS(text)
    tts.save('temp.mp3')  #.mp3 used with pygame
    
    pygame.mixer.init()            # initialize sound system
    pygame.mixer.music.load("temp.mp3")  # path to your mp3
    pygame.mixer.music.play()      #play the mp3 file

    # keep program alive while music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
    
    
    
def aiProcess(command):
    client = OpenAI(
    api_key="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",
    )
    completion = client.chat.completions.create( 
    model="gpt-5-nano", 
    messages=[ 
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. give short responses"}, 
        {"role": "user", "content": "what is coding"} 
        ]
    )
    return completion.choices[0].message.content
    
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]  #converting into list
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #parse the JSON response
            data = r.json()
            
            #extract the articles
            articles = data.get('articles', [])
            
            #print the headlines
            for article in articles:
                speak(article['title'])
    else:
        #let openAI handle the request
        output = aiProcess(c)
        speak(output)


r = sr.Recognizer()

if __name__ == "__main__":
    speak("initializing....kese ho")  #yaha tak bolna start kar diya hai
    #listen for the wake word "edith"
    
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        
        print("recognizing...")
        try:
            with sr.Microphone() as source: #listen fro command for 1st time
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=1) #will adjust for low audio also
                audio = r.listen(source, timeout=5, phrase_time_limit=2) # will listen till 5 secs, 
            word = r.recognize_google(audio) #voice recognize function of google, we can use from so many
            print(word)
            speak(word)
            if word.lower() == "friday": #if command friday hua
                speak("wake word detected")                  #so wo kahega ya
                #listen for command again
                with sr.Microphone() as source:
                    print("Friday Active...")
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source, timeout=5, phrase_time_limit=2)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                                     
        except Exception as e:
            print("Error; {0}".format(e))  #will throw error if audio is not clear or not heard properly
    
