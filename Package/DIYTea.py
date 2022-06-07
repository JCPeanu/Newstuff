import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QDial, QLCDNumber, QLineEdit
 
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() #The MainWindow is actually a QMainWindow
        self.setWindowTitle("DIY tea") #Window Title
 
        main_layout = QVBoxLayout() #The main layout is vertical
        layout_type = QHBoxLayout() #Choosing type of tea layout
        layout_temp = QHBoxLayout() #Choosing temperature layout
        layout_name = QHBoxLayout() #Inputting user's name
 
        #Filling the first layout about choosing type of tea
        #A simple label
        layout_type.addWidget(QLabel("Type of tea"))
        #A dropdown chooser, I had to set it as object property as it's used in a method
        self.types = QComboBox()
        self.types.addItems(["Black", "Green", "White", "Oolong"])
        layout_type.addWidget(self.types)
        #A text that will change depending on the type picked
        self.advise = QLabel()
        self.types.currentTextChanged.connect(self.change_advise) #implicit method call
        layout_type.addWidget(self.advise)
 
        #adding the type of tea layout to the main layout
        main_layout.addLayout(layout_type)
 
        #Now proceeding to the temperature layout
        #A simple label
        layout_temp.addWidget(QLabel("Temperature (C)"))
        #Adjust the temperature with a dial
        self.dial = QDial()
        self.dial.setRange(0, 60)
        layout_temp.addWidget(self.dial)
        #And display the dial's number using the LCD number display
        self.lcd_display = QLCDNumber()
        layout_temp.addWidget(self.lcd_display)
        self.dial.sliderMoved.connect(self.lcd_display.display)
 
        #add that horizontal layout to the main vertical layout
        main_layout.addLayout(layout_temp)
 
        #Now for the name layout
        layout_name.addWidget(QLabel("Your name: "))
        #Allow the user to write its name
        self.name = QLineEdit()
        layout_name.addWidget(self.name)
        #Add the order button
        self.ok = QPushButton("Order!")
        layout_name.addWidget(self.ok)
        #Add the sublayout to the main one
        main_layout.addLayout(layout_name)
 
        #Finally add a single widget which displays the confirmation order message
        self.confirmation = QLabel()
        self.ok.pressed.connect(self.print_receipt)  # implicit method call
        main_layout.addWidget(self.confirmation)
 
        #Now create a macro widget that contains everything
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
 
    #This method will change the text displayed depending on the tea choice
    def change_advise(self):
        if self.types.currentText() == "Black":
            self.advise.setText("For the flavor!")
        elif self.types.currentText() == "Green":
            self.advise.setText("For the weight loss!")
        elif self.types.currentText() == "White":
            self.advise.setText("Anti-aging!")
        elif self.types.currentText() == "Oolong":
            self.advise.setText("A chinese tradition!")
 
    #This method changes the confirmation order message
    def print_receipt(self):
        message = self.types.currentText() #Get type of tea
        message += " tea for " + self.name.text() + " coming right up!"
        self.confirmation.setText(message)
 
#Declare the app
app = QApplication(sys.argv)
 
#Create and show the MainWindow object we previously defined
window = MainWindow()
window.show()
 
#Run the app
app.exec()