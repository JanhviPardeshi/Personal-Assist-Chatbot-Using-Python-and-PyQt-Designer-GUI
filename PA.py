import pyttsx3 # text to speech converter
import pywhatkit # send message 
import pywhatkit as kit # for open YouTube
import speech_recognition as sr # for recognizing voice in hindi,english
import datetime   # for current date and time 
import pyjokes  # For random jokes
import time # Current time
import sys # for system commands
import tkinter as tk # For GUI, use for file explorer
from tkinter import filedialog # Filedialog= File explorer
# import database.extrapro.start
from pywikihow import search_wikihow, WikiHow # Special function for "How" type of questions
# from ast import Return , Try 
# -------------------
from bs4 import BeautifulSoup
# -------------------
# from email.mime import audio 
import requests  # For finding locations or finding IP address
import random # For selection of random output
import wikipedia  # To access the data from wikipedia
import webbrowser # For interfacing to allow web based documents to user
import os # To interact with the Operating System 
import pyautogui # Here for taking screenshots
import PyPDF2 # For  reading , writing and extracting the data of pdfs
from PyQt5 import QtWidgets, QtCore, QtGui 
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie # For Animation in GUI
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * #For labels and buttons of GUI
from PyQt5.uic import loadUiType # user interface compiler ....use to compile the code and here,(converts in the python file)
from personalAssistant import Ui_PersonalAssistant_ # importing the class in personalAssistant.py


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <= 12:
        speak("good morning")
    elif hour >12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("what can i do for you ?")

def pdf_reader():

    root = tk.Tk() 
    root.withdraw() 
    pdf = filedialog.askopenfilename()

    pdfreader = PyPDF2.PdfReader(pdf,'rb')

    pages = len(pdfreader.pages)

    speak(f"total number of pages in this book {pages} ")

    page = pdfreader.pages[1]
    text = page.extract_text()
    speak(text)


class MainThread(QThread):
   
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.search()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=6, phrase_time_limit=6)

        try:
            print("Recognizing...")
            Query = r.recognize_google(audio, language='en-in')
            print(f"user said: {Query}")

        except Exception as e:
            speak("say that again please ..")
            return "none"
        return Query
    
    def takecommand_hindi(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=6, phrase_time_limit=6)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language='hi')
            print(f"user said: {query}")

        except Exception as e:
            speak("say that again please ..")
            return "none"

        return query


    def search(self):
        wish()
        while True:
            self.Query = self.takecommand().lower()
            # if self.Query in self.Query:
            #     self.googlesearch(self.Query)
            self.query = self.Query.replace("what is", "")
            self.query = self.Query.replace("how to", "")
            self.query = self.Query.replace("when was", "")
            self.query = self.Query.replace("where was", "")
            self.query = self.Query.replace("what do you mean by", "")

            writeab = str(self.Query)
            ooop = open("data.txt", "a")
            ooop.write(writeab + "\n")
            ooop.close()

            if 'how to' in self.query:
                max_res = 1
                howtofunc = search_wikihow(query=self.query,max_results=max_res)
                assert len(howtofunc) == 1
                # howtofunc[0].print()
                speak(howtofunc[0].summary)

            if 'what is' in self.query:
                pywhatkit.search(self.query)
                search = wikipedia.summary(self.query,2)
                speak(f"according to your search : {search}")
            
            if 'when was' in self.query:
                 pywhatkit.search(self.query)
                 search = wikipedia.summary(self.query,2)
                 speak(f"according your search : {search}")
            if 'where was' in self.query:
                 pywhatkit.search(self.query)
                 search = wikipedia.summary(self.query,2)
                 speak(f"according your search : {search}")

            if 'what do you mean by' in self.query:
                 pywhatkit.search(self.query)
                 search = wikipedia.summary(self.query,2)
                 speak(f"according your search : {search}")

# ================================================================================================
            elif "open notepad" in self.Query:
                    path = "C://Windows//system32//notepad.exe"
                    os.startfile(path)
           
            elif 'open youtube' in self.Query:
                    webbrowser.open("https://www.youtube.com/")
                    speak('opening youtube...')

            elif 'open stack overflow' in self.Query:
                    webbrowser.open("https://stackoverflow.com/")
                    speak('opening stackoverflow...')

            elif 'play music' in self.Query or 'play some songs' in self.Query:
                    webbrowser.open("https://www.youtube.com/watch?v=D-YDEyuDxWU")
                    speak('playing music on youtube...')

            elif "what's the time" in self.Query or 'what is the time' in self.Query or "time" in self.Query:
                    strtime = datetime.datetime.now().strftime("%H hour  %M minutes  %S seconds")
                    speak(f'the time is {strtime}')

            elif "open lt spice" in self.Query:
                    ltspicepath = "C:\\Program Files\\LTC\\LTspiceXVII\\XVIIx64.exe"
                    os.startfile(ltspicepath)
                    speak('opening lt spice...')

            elif 'open docs'  in self.Query or 'open google docs'  in self.Query:
                    webbrowser.open("https://docs.google.com/forms/u/0/?tgif=d")
                    speak('opening docs...')

            elif 'open meet' in self.Query:
                    webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")
                    speak('opening google meet...')

            elif 'open display settings' in self.Query:
                    a = "C://Windows//System32//DpiScaling.exe"
                    os.startfile(a)
                    speak('opening display settings...')
                
            elif 'tell me a joke' in self.Query or 'tell a joke' in self.Query or 'joke' in self.Query or 'another joke' in self.Query:
                joke = pyjokes.get_joke()
                speak(joke)
# task++++=========================================================
            elif 'open c drive' in self.Query:
                    b = "C:"
                    os.startfile(b)
                    speak('opening c drive..')
            #  if the drive not available what to do         
            elif 'open d drive' in self.Query:
                    b = "D:"
                    os.startfile(b) 
                    speak('opening d drive..')
# ==================================================================
            elif 'shutdown the system' in self.Query or 'shutdown the pc' in self.Query or 'shutdown' in self.Query or 'turn off the pc' in self.Query:
                speak("really want to shutdown please say yes, othervise  no")
                tc = self.takecommand().lower()
                if 'yes' in tc or 'yes please' in tc:
                    os.system("shutdown /s /t 3")
                else:
                    speak("okay")
# task++++=========================================================

            elif 'sleep the system' in self.Query or 'sleep the pc' in self.Query :
                os.system("rundll32.exe powrprof.dll, setsuspendstate 0 ,1, 0")

            elif 'open command prompt' in self.Query:
                os.system("start cmd")

            elif 'open e drive' in self.Query:
                    b = "E:"
                    if os.startfile(b) == True:
                        os.startfile(b)
                        speak('opening d drive..')
                    else:
                        speak('drive not exist..')
            
            elif 'open wikipedia' in self.Query:
                 speak("what you want to search on wikipedia ")
                 a = self.takecommand().lower()
                 wikipedia.search(a)

# task++++=========================================================

# open file explorer ..... 
            elif 'open downloads' in self.Query:
                    down = 'C://Users//ACER//Downloads'
                    os.startfile(down)
                    speak("opening downloads..")

            elif 'open documents' in self.Query:
                    down = 'C://Users//ACER//OneDrive//Documents'
                    os.startfile(down)
                    speak("opening documents..")

            elif 'open pictures' in self.Query:
                    down = 'C://Users//ACER//OneDrive//Pictures'
                    os.startfile(down)
                    speak("opening pictures..")
            elif 'open screenshots' in self.Query:
                    down = 'C://Users//ACER//OneDrive//Pictures//Screenshots'
                    os.startfile(down)
                    speak("opening screenshots..")
            # elif 'play some music' in self.Query:
                 

            elif 'open google' in self.Query:
                speak("what should i search on google ")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif'who am i' in self.Query:
                 speak("you didn't tell me your name")

            elif 'send message' in self.Query or 'send message in whatsapp' in self.Query:
                cont = {"aadesh":8999809346,"janhvi":7887763669,"nikhil":8975405758} 
                speak("whom do you want to send messege")
                gt = self.takecommand().lower()
                print(gt)
                if gt in cont.keys():
                    print(cont[gt])
                    strtime = datetime.datetime.now().strftime("%H")
                    strtime1 = datetime.datetime.now().strftime("%M")
                    print(strtime)
                    print(strtime1)
                    a = int(strtime)
                    b = int(strtime1)
                    speak("please say the message")
                    mg = self.takecommand().lower()
                    pywhatkit.sendwhatmsg(f"+91{cont[gt]}",mg,a,b+1)

                    speak("message sent successfully..")
                else:
                    speak("contact not found")
                
            elif 'thank you' in self.Query or 'thanks' in self.Query or 'thank you so much' in self.Query or 'nice' in self.Query:
                grd = ['glad to help you','welcome','always there for you','anytime']
                a = random.choice(f"{grd}")
                speak(a)

            elif 'play song on youtube' in self.Query or 'play video on youtube' in self.Query or 'play music on youtube' in self.Query  or 'play some music' in self.Query:
                speak("which song you want to play")
                gt = self.takecommand().lower()
                pywhatkit.playonyt(gt)

            elif 'play something on youtube' in self.Query:
                speak("what you want to play")
                gt = self.takecommand().lower()
                kit.playonyt(gt)

            elif 'where am i' in self.Query or 'where i am' in self.Query or 'my location' in self.Query or 'whats is my location' in self.Query:
                speak("please wait ")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    georeq = requests.get(url)
                    geo_data=georeq.json()

                    city = geo_data['city']

                    country = geo_data['country']

                    speak(f"the location is {city} city of {country} country")
                except Exception as e:
                    speak("Network error..")
                    pass
            elif 'take a screenshot' in self.Query or 'take screenshot' in self.Query or 'take snapshot' in self.Query:
                speak("tell me the name for this file to save")
                name = self.takecommand().lower()
                speak("hold on the screen for few seconds, while taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("screenshot successfully saved in main folder")

            elif 'read pdf for me' in  self.Query or 'read pdf' in self.Query:
                speak("please select the pdf to read")
                pdf_reader()

            elif 'okay' in self.Query:
                 greed = ['cool', 'perfect', "i'm happy to hear that", 'yes']
                 a = random.choice(greed)
                 speak(a)
            
            # elif "temperature" in self.Query:
            #     srch = "temperature in nagpur "
            #     urll = f"https://www.google.com/search=?q={srch}"
            #     r = requests.get(urll)
            #     data = BeautifulSoup(r.text,"html.parser")
            #     tmp =data.find("div",class_="BNeawe").text
            #     speak(f"current {srch} is {tmp}")

            elif "my battery percent" in self.Query or "battery percent" in self.Query or " check my battery percent" in self.Query:
                import psutil
                battery = psutil.sensors_battery()
                percent = battery.percent
                if percent == 100:
                     speak(f"i am fully charged with {percent} percent")
                elif percent > 70 :
                    speak(f"i have {percent} percent battery remaining")
                elif 30 < percent < 70:
                     speak(f"battery is {percent} percent")
                else:
                    speak(f"battery is {percent} percent  i am about to die please charge")

            elif "internet speed" in self.Query or "internet speed test" in self.Query or "internet speed test " in self.Query or "check internet speed" in self.Query or "my internet speed" in self.Query or "check my internet speed" in self.Query:
                import speedtest
                speak("wait while checking , it will take few seconds")
                s1 = speedtest.Speedtest()
                d1 = s1.download()
                do = d1/1000000
                u1 = s1.upload()
                up = u1/1000000
                
                speak(f"uploading speed is {round(up,ndigits=3)} MB Per Seconds and \ndownloading speed is {round(do,ndigits=3)} MB per seconds")


            elif 'stop' in self.Query or 'exit' in self.Query:
                greed = ['nice to meet you', 'thank you', 'sure', 'glad to help you',"i'm happy to hear that"]
                a = random.choice(greed)
                speak(a)
                # print(a)
                # exit(app.exec_())
                sys.exit(0)

            

            
            


# if __name__ == "__main__":
startExex = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PersonalAssistant_()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.startTask) # run button to start everything 
        self.ui.pushButton_2.clicked.connect(self.close) # exit click

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\GUI\gifs\icon.gif")
        self.ui.PersonalAssistant.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:\GUI\gifs\loading.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:\GUI\gifs\ace-ace-v2.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)

        timer.start(1)

        startExex.start()  # mainthread jaha pe pura backend likha hei for voices

    def showtime(self):
        curr_time = QTime.currentTime()
        curr_date = QDate.currentDate()

        label_time = curr_time.toString('hh:mm:ss')
        label_date = curr_date.toString(Qt.ISODate)

        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)


app = QApplication(sys.argv)
personal_assist = Main()
personal_assist.show()

sys.exit(app.exec_())
