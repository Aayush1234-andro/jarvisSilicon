import imp
from JarvisUi import Ui_JarvisUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5 .QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import jarvis
import os
import webbrowser as web
import sys

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        

    def run(self):
        jarvis.TaskExecution()
        

startExecution = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()   
        


        self.gui = Ui_JarvisUi()
        self.gui.setupUi(self)

        self.gui.Start.clicked.connect(self.startTask)
        self.gui.Quit.clicked.connect(self.close)
        self.gui.Wikipedia.clicked.connect(self.wikipedia_app)
        self.gui.Spotify.clicked.connect(self.spotify_app)
        self.gui.Vscode.clicked.connect(self.vscode_app)
        self.gui.Youtube.clicked.connect(self.youtube_app)
    
    def wikipedia_app(self):
        web.open("https://www.wikipedia.org/")

    def youtube_app(self):
        web.open("https://www.youtube.com")

    def spotify_app(self):
        web.open("https://spotify.com/")      

    def vscode_app(self):
        os.startfile("C:\\Users\\91916\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")     

    def startTask(self):

        self.gui.label1 = QtGui.QMovie("G.U.I Material//ExtraGui//Health_Template.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("G.U.I Material//ExtraGui//Hero_Template.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("G.U.I Material//ExtraGui//Earth.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("G.U.I Material//ExtraGui//live.gif")
        self.gui.Gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5 = QtGui.QMovie("G.U.I Material//ExtraGui//Code_Template.gif")
        self.gui.Gif_5.setMovie(self.gui.label5)
        self.gui.label5.start()

        self.gui.label6 = QtGui.QMovie("G.U.I Material//VoiceReg//Ntuks.gif")
        self.gui.Gif_6.setMovie(self.gui.label6)
        self.gui.label6.start()

        self.gui.label7 = QtGui.QMovie("G.U.I Material//ExtraGui//initial.gif")
        self.gui.Gif_7.setMovie(self.gui.label7)
        self.gui.label7.start()

        self.gui.label8 = QtGui.QMovie("G.U.I Material//ExtraGui//B.G_Template_1.gif")
        self.gui.Gif_8.setMovie(self.gui.label8)
        self.gui.label8.start()

        self.gui.label9 = QtGui.QMovie("G.U.I Material//ExtraGui//Jarvis_Gui (2).gif.gif")
        self.gui.Gif_9.setMovie(self.gui.label9)
        self.gui.label9.start()

        startExecution.start()

GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.showFullScreen()
exit(GuiApp.exec_())   