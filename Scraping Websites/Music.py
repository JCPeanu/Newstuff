import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QDial, QLCDNumber, QLineEdit, QDialog, QScrollArea
from PyQt6.QtGui import QPixmap, QFont
import requests
from bs4 import BeautifulSoup #this package can understand HTML code

class AnotherWindow(QDialog):
    #This "window" is a QWidget. If it has no parent, it
    #will appear as a free-floating window as we want.
 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search for Lyrics")
        layout = QVBoxLayout()
        Line1 = QHBoxLayout()
        Line2 = QHBoxLayout()
        Line3 = QHBoxLayout()

        self.label1 = QLabel("Song Artist: ")
        Line1.addWidget(self.label1)

        self.Artist = QLineEdit()
        Line1.addWidget(self.Artist)

        layout.addLayout(Line1)

        self.label2 = QLabel("Song Title: ")
        Line2.addWidget(self.label2)

        self.title = QLineEdit()
        Line2.addWidget(self.title)

        layout.addLayout(Line2)

        self.get = QPushButton("Find!")
        self.resetit = QPushButton("Reset")
        self.answer = QLabel()
        Line3.addWidget(self.get)
        Line3.addWidget(self.resetit)
        layout.addLayout(Line3)
        self.get.pressed.connect(self.Find)

        layout.addWidget(self.answer)

        self.resetit.pressed.connect(self.reset)

        self.setLayout(layout)

    def Find(self):
        address = 'http://api.chartlyrics.com/apiv1.asmx/SearchLyricDirect?artist="{}"&song="{}"'.format(self.Artist.displayText(), self.title.displayText())
        self.SearchLyrics = requests.get(address)
        soup = BeautifulSoup(self.SearchLyrics.content, 'xml')
        self.answer.setText(soup.find("Lyric").text)
    def reset(self):
        self.Artist.setText("")
        self.title.setText("")
        self.answer.setText("")
        self.setGeometry(550,300,250,150)
        
class ThirdWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search for Songs and Artists")
        layout = QVBoxLayout()
        Line1 = QHBoxLayout()
        Line2 = QHBoxLayout()

        self.label = QLabel("Lyrics: ")
        Line1.addWidget(self.label)

        self.lyrics = QLineEdit()
        Line1.addWidget(self.lyrics)

        layout.addLayout(Line1)

        self.get = QPushButton("Find!")
        self.resetit = QPushButton("Reset")
        Line2.addWidget(self.get)
        Line2.addWidget(self.resetit)
        self.answer = QLabel()
        layout.addLayout(Line2)

        self.get.pressed.connect(self.Find)
        layout.addWidget(self.answer)
        self.resetit.pressed.connect(self.reset)
        self.setLayout(layout)

    def Find(self):
        address = 'http://api.chartlyrics.com/apiv1.asmx/SearchLyricText?lyricText="{}"'.format(self.lyrics.displayText())
        self.SearchLyrics = requests.get(address)
        soup = BeautifulSoup(self.SearchLyrics.content, 'xml')
        message = "Artist: " + soup.find("Artist").text + "\nSong: " + soup.find("Song").text
        self.answer.setText(message)
    def reset(self):
        self.lyrics.setText("")
        self.answer.setText("")
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() #The MainWindow is actually a QMainWindow
        self.setWindowTitle("Music") #Window Title
 
        main_layout = QVBoxLayout() #The main layout is vertical
        layout_type = QHBoxLayout() #Choosing type of tea layout

        #Filling the first layout about choosing type of tea
        #A simple label
        layout_heading = QVBoxLayout()
        self.title = QLabel("You got two options. I'm going to seasrch through a music website and give you the result.")
        self.title.setFont(QFont('Times New Roman', 20))
        layout_heading.addWidget(self.title)
        main_layout.addLayout(layout_heading)

        #A dropdown chooser, I had to set it as object property as it's used in a method
        self.one = QPushButton("Search for the lyrics")
        self.two = QPushButton("Search for the name of the song")
        layout_type.addWidget(self.one)
        layout_type.addWidget(self.two)

        self.one.pressed.connect(self.show_second_window)
        self.two.pressed.connect(self.show_third_window)

    #     #A text that will change depending on the type picked
    #     self.advise = QLabel()
    #     self.types.currentTextChanged.connect(self.change_advise) #implicit method call
    #     layout_type.addWidget(self.advise)
 
        main_layout.addLayout(layout_type)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
    def show_second_window(self):
        self.w = AnotherWindow()
        self.w.show()
    def show_third_window(self):
        self.w = ThirdWindow()
        self.w.show()
#Declare the app
app = QApplication(sys.argv)
 
#Create and show the MainWindow object we previously defined
window = MainWindow()
window.show()
 
#Run the app
app.exec()