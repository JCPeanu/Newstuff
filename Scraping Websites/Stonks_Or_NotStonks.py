import sys
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
 
import requests #to interact with the internet
from bs4 import BeautifulSoup #this package can understand HTML code
 
#first tell requests to get the webpage info


#print(soup.prettify())
#print(soup.findAll('h1'))
#print(soup.find('h1', {'class': 'company__name'}).text)
 
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "Stock prices"
        self.setWindowTitle(self.title)
 
        self.URL = "https://www.marketwatch.com/investing/stock/gme"
        self.web = requests.get(self.URL)
        self.soup = BeautifulSoup(self.web.content, 'html.parser')

        main_layout = QVBoxLayout()
        question = QVBoxLayout()
        question.addWidget(QLabel("Ticker of the company: "))
        self.answer = QLineEdit()
        question.addWidget(self.answer)

        self.ok = QPushButton("Find!")
        question.addWidget(self.ok)

        main_layout.addLayout(question)

        self.price = self.soup.find('bg-quote', {'format': '0,0.00', 'field': 'Last'}).text
        self.percent = self.soup.find('bg-quote', {'format': '0,0.00%', 'session': 'after'}).text

        self.ok.pressed.connect(self.getStuff)  # implicit method call

        main_layout.addLayout(question)
        self.current_price = QLabel(self.price)
        self.current_price.setFont(QFont('Arial', 40))
        self.current_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.current_price)

        self.reaction = QLabel(self)
        self.stonks = QPixmap('stonks.png')
        self.not_stonks = QPixmap('not_stonks.png')
        if (self.percent[0] == "-"):
            self.reaction.setPixmap(self.not_stonks)
        else:
            self.reaction.setPixmap(self.stonks)
 
        main_layout.addWidget(self.reaction)
 
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def getStuff(self):
        self.URL = "https://www.marketwatch.com/investing/stock/" + self.answer.text()
        self.web = requests.get(self.URL)
        self.soup = BeautifulSoup(self.web.content, 'html.parser')
        self.price = self.soup.find('bg-quote', {'format': '0,0.00', 'field': 'Last'}).text
        self.percent = self.soup.find('bg-quote', {'format': '0,0.00%', 'session': 'after'}).text
        self.current_price.setText(self.price)
        if (self.percent[0] == "-"):
            self.reaction.setPixmap(self.not_stonks)
        else:
            self.reaction.setPixmap(self.stonks)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
 
