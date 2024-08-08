import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import os
import os.path
import cv2
import requests
import wikipedia
import pywhatkit as kit
import smtplib
import pyautogui as pg
import sys
import pyjokes
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from JarvisUi import Ui_jarvisUi
import Jarvis



engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voices", voices[1].id)





class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.startTask)
        
    #wish()
    #audio1=takeCommand()
    #speak(audio1)
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
        print(audio)
    def sendEmail(to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("Tripti.052002@gmail.com","lhuo sxho tkzx bhpd")
        server.sendmail("Tripti.052002@gmail.com",to,content)
        server.close()

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source,timeout=5)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language="en-in")
                print(f"User said: {query}")
                return query
            except Exception as e:
                return "Say that again Please..."
    class MainThread(QThread):
        def __init__(self) :
            super(MainThread,self).__init__()
        def Run(self):
            self.main()
    def wish():
        hour=(datetime.datetime.now().hour)
        if hour>=0 and hour<=12:
            self.speak("good morning")
        elif hour>12 and hour<18:
            self.speak("good afternoon")
        else:
            self.speak("good evening")
        self.speak("I am jarvis boss , please tell me how can i help you")

    startExecution = MainThread()

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\ANJALI\\Downloads\\7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\ANJALI\\Downloads\\Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        # timer= QTimer(self)
        # timer.timeout.connect(self.showtime)
        # timer.start(1000)
        self.startExecution.start()

    def showtime(self):
        current_time = QTime.currentTime
        current_date = QDate.currentDate
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ItemSelectionOperationDate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.orig_argv)
jarvis =Main()
jarvis.show()
exit(app.exec_())

        
               
        
        
         
        