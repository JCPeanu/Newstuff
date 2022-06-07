from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,\
    QHBoxLayout,QRadioButton,QGroupBox , QLabel, QButtonGroup, QCheckBox
from PyQt6.QtGui import QIcon, QFont, QPixmap
import sys
import random
from time import sleep


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.mycount = 0
        self.compcount = 0
        self.setWindowTitle("Rock Paper Scissors")
        self.setGeometry(500,200,300,300)
        self.radio_btn()
        vbox = QVBoxLayout()
        vbox.addWidget(self.grpbox)

        self.Scores = QLabel("My Score: " + str(self.mycount) + "\tComputer Score: " + str(self.compcount))
        self.Scores.setFont(QFont("Times New Roman", 24))
        vbox.addWidget(self.Scores)

        # this is our label
        self.label = QLabel("Sup! Want to play a game?")
        self.label.setFont(QFont("Times New Roman", 48))

        # add your widgets in the vbox layout
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.Pic = QLabel()
        self.YouWin = QPixmap("YouWin.png")
        self.Tie = QPixmap("Atie.jpeg")
        self.YouLost = QPixmap("Lost.jpeg")
        vbox.addWidget(self.Pic)

    def radio_btn(self):
        self.checkbox_confirmed = QCheckBox('Confirmed')
        self.grpbox = QGroupBox("Choose Your Moves ")
        self.grpbox.setFont(QFont("Times New Roman", 15))

        # this is hbox layout
        hbox = QHBoxLayout()

        self.RadioGroup = QButtonGroup()

        # these are the radiobuttons
        self.rad0 = QRadioButton("Reset")
        self.rad0.setFont(QFont("Times New Roman", 14))
        self.RadioGroup.addButton(self.rad0)

        self.rad10 = QRadioButton("Continue")
        self.rad10.setFont(QFont("Times New Roman", 14))
        self.RadioGroup.addButton(self.rad10)

        self.rad1 = QRadioButton("Rock")
        self.rad1.setFont(QFont("Times New Roman", 14))
        self.RadioGroup.addButton(self.rad1)

        self.rad2 = QRadioButton("Paper")
        self.rad2.setFont(QFont("Times New Roman", 14))
        self.RadioGroup.addButton(self.rad2)

        self.rad3 = QRadioButton("Scissors")
        self.rad3.setFont(QFont("Times New Roman", 14))
        self.RadioGroup.addButton(self.rad3)

        if(self.rad10.checkStateSet):
            self.rad10.toggled.connect(self.initialize)

        if(self.rad0.checkStateSet):
            self.rad0.toggled.connect(self.initialize)
            self.rad0.toggled.connect(self.Reset)

        self.rad1.toggled.connect(self.on_selected)

        self.rad2.toggled.connect(self.on_selected)
        
        self.rad3.toggled.connect(self.on_selected)

        hbox.addWidget(self.rad0)
        hbox.addWidget(self.rad10)
        hbox.addWidget(self.rad1)
        hbox.addWidget(self.rad2)
        hbox.addWidget(self.rad3)

        self.grpbox.setLayout(hbox)

    def initialize(self):
        self.RadioGroup.setExclusive(False)
        self.rad1.setChecked(False)
        self.rad2.setChecked(False)
        self.rad3.setChecked(False)
        self.RadioGroup.setExclusive(True)

    def Reset(self):
        self.mycount = 0
        self.compcount = 0
        self.label = QLabel("Sup! Want to play a game?")
        self.label.setFont(QFont("Times New Roman", 48))

    # method or slot for the toggled signal
    def on_selected(self):
        self.label.setFont(QFont("Times New Roman", 15))
        self.setGeometry(500,200,300,300)
        radio_button = self.sender()
        lst = ["Rock", "Paper", "Scissors"]
        if radio_button.isChecked():
            r1 = random.randint(0, 2)
            # self.label.setText("You have selected : " + radio_button.text() + "\nThe computer has selected : " + lst[r1] + "\nWait...")
            move = radio_button.text()
            comp_move = lst[r1]

            if move == "Rock" and comp_move == "Paper":
                self.label.setText("You have selected : " + radio_button.text() + "\nThe computer has selected : " + lst[r1] + "\nWait..." + "\nYou've Lost!")
                self.Pic.setPixmap(self.YouLost)
                self.compcount += 1
            elif move == "Rock" and comp_move == "Scissors":
                self.label.setText("You have selected : " + radio_button.text() + "\nThe computer has selected : " + lst[r1] + "\nWait..." + "\nYou've Won!")
                self.Pic.setPixmap(self.YouWin)
                self.mycount += 1
            elif move == "Rock":
                self.label.setText("You have selected : " + radio_button.text() + "\nThe computer has selected : " + lst[r1] + "\nWait..." + "\nIt's a Tie!")
                self.Pic.setPixmap(self.Tie)
            elif move == "Scissors" and comp_move == "Paper":
                self.label.setText("You have selected : " + radio_button.text() + "\nThe computer has selected : " + lst[r1] + "\nWait..." + "\nYou've Won!")
                self.Pic.setPixmap(self.YouWin)
                self.mycount += 1
            elif move == "Scissors" and comp_move == "Rock":
                self.label.setText("You have selected : " + radio_button.text() + "\nThe computer has selected : " + lst[r1] + "\nWait..." + "\nYou've Lost!")
                self.Pic.setPixmap(self.YouLost)
                self.compcount += 1
            elif move == "Scissors":
                self.label.setText("You have selected : " + radio_button.text() + "\nThe computer has selected : " + lst[r1] + "\nWait..." + "\nIt's a Tie!")
                self.Pic.setPixmap(self.Tie)
            elif move == "Paper" and comp_move == "Scissors":
                self.label.setText("You have selected : " + radio_button.text() + "\nThe computer has selected : " + lst[r1] + "\nWait..." + "\nYou've Lost!")
                self.Pic.setPixmap(self.YouLost)
                self.compcount += 1
            elif move == "Paper" and comp_move == "Rock":
                self.label.setText("You have selected : " + radio_button.text() + "\nThe computer has selected : " + lst[r1] + "\nWait..." + "\nYou've Won!")
                self.Pic.setPixmap(self.YouWin)
                self.mycount += 1
            elif move == "Paper":
                self.label.setText("You have selected : " + radio_button.text() + "\nThe computer has selected : " + lst[r1] + "\nWait..." + "\nIt's a Tie!")
                self.Pic.setPixmap(self.Tie)
            self.Scores.setText("My Score: " + str(self.mycount) + "\tComputer Score: " + str(self.compcount))



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())