###################################### 
#          T A R S - A  I            #
#          Author: naqviO7           #
#          Version: 1.0              #
###################################### 

#STARTOFCODE 
import os 
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr

#creating instance of pyttsx3 module
engine=pyttsx3.init()


#simple intro for TARS AI
def Introduce():
    engine.say('Hello, I am TARS, your Desktop Assistant!, My Current Version 1.0')
    engine.say('I was Develloped by Saqlain Naqvi')
    engine.say('I was Created after getting Inspiration from Interstellar Movie!')
    engine.say('I am Here to Make Things Easy for You!')
    engine.say('You can Give me Commands that are Coded in ME!') 
    engine.runAndWait()


#speak function 
#takes arguement in string format and outputs as audio
def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function to take command from user in audio format
#requires internet connection


def TakeCommand():
    aud = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        aud.pause_threshold = 1
        audio = aud.listen(source)

    try:
        query = aud.recognize_google(audio, language='en-us')
        print('Your Command:', query)
        Speak(query)

    except Exception as e:
        Speak('Say Again Please!')
        Speak('Getting Error!')
        return 'None'

    return query


#wihsmefunction
#wishes acoriding to time of day
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak('Good Morning!, Have Nice Day!')

    elif hour >= 12 and hour < 17:
        Speak('Good Afternoon!')

    elif hour >= 17 and hour < 19:
        Speak('Good Evening!, How Was Your Day?')

    else:
        Speak('Good Night!, Have a Nice Sleep!')


#time function 
#tells time in hours:minutes:seconds formats
def TellTime():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    Speak(Time)
    

#function to make ai to rember things
#things it has to remmeber will be stored in a text file
#wen asked it will check and tell 
def RememberIt():
    Speak('What Should I Remember?')
    data=TakeCommand()
    Speak('You Said Me to Remeber That' + data)
    remember=open('RememberThingsFile.txt','w')
    remember.write(data)
    remember.close()
 
 
#function to tell what i asked ai to remember    
def DoKnowAnyThing():
    remember=open('RememberThingsFile.txt','r')
    Speak('You Said Me to Remeber That'+remember.read()) 
    remember.close()   
 
    
#date function 
#tells current date to user
def TellDate():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    
    Speak('Date is')
    Speak(day)
    Speak(month)
    Speak(year)
 

#search function 
#able to search for anything on wikipedia
def WikipediaSearch():
    Speak('Searching On Wikipedia') 
    qury=query.replace('wikipedia','')
    result=wikipedia.summary(qury,sentences=2)
    print(result)
    Speak(result)


#function to open google chrome     
def OpenGoogle():
    url = "google.com"
    chromepath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromepath))
    webbrowser.get('chrome').open_new_tab(url)


#function to open facebook in google chrome 
def OpenFacebook():
    url = "https://www.facebook.com"
    chromepath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
    webbrowser.get('chrome').open_new_tab(url)
    

#function to open instagram in google chrome 
def OpenInstagram():
    url = "https://www.instagram.com"
    chromepath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
    webbrowser.get('chrome').open_new_tab(url)
    
#function to open github in google chrome 
def OpenGithub():
    url='https://www.github.com'
    chromepath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
    webbrowser.get('chrome').open_new_tab(url)


#function to open stackoverflow in google chrome 
def OpenStackOverflow():
    url = 'https://stackoverflow.com'
    chromepath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
    webbrowser.get('chrome').open_new_tab(url)


#function to open youtube in google chrome 
def OpenYoutube():
    url = 'https://youtube.com'
    chromepath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
    webbrowser.get('chrome').open_new_tab(url)


#main function
if __name__=='__main__':
    Introduce()
    while True:
        query=TakeCommand()
        
        if 'hello' in query:
            Speak('Hello! How may I Help You!')
        
        elif 'who are you' in query:
            Speak('I am Tars, Your Virtual Desktop Assistant!')
        
        elif 'time' in query:
            TellTime()
        
        elif 'date' in query:
            TellDate()
        
        elif 'search in wikipedia' in query:
            WikipediaSearch()
        
        elif 'open google' in query:
            OpenGoogle()
        
        elif 'open facebook' in query:
            OpenFacebook()
        
        elif 'open instagram' in query:
            OpenInstagram()
        
        elif 'open youtube' in query:
            OpenYoutube()
            
        elif 'remember it' in query:
            RememberIt()

        elif 'do you know any thing' in query:
            DoKnowAnyThing()
            
        elif 'turn off' in query:
            Speak('Turning Off the Computer!')
            os.system('shutdown /s /t 1')
           
        elif 'restart' in query:
            os.system('shutdown /r /t 1')
        
        elif 'logout' in query:
            os.system('shutdown -l')
        
        elif 'exit' in query or 'stop' in query or 'quit' in query or 'go offline' in query:
            exx_exit = 'Closing My Self!,See you soon. Takecare!'
            Speak(exx_exit)
            print('Good Bye!')
            exit()
#ENDOFCODE
