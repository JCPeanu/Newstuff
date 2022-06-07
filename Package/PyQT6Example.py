#Examples shamelessly taken from
#https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/
 
#Example 1. First app... just an empty window
"""
# import the application handler and widget GUI
from PyQt6.QtWidgets import QApplication, QWidget
# The main modules for Qt are QtWidgets, QtGui and QtCore.
 
# Only needed for access to command line arguments
import sys
 
# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)
 
# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT! Windows are hidden by default.
 
# Start the event loop.
app.exec()
 
# Your application won't reach here until you exit and the event
# loop has stopped.
print("Program ended.")
"""
 
#Example 2. A button.
"""
import sys
#Now, instead of a widget, our window is going to be a single button
from PyQt6.QtWidgets import QApplication, QPushButton
 
app = QApplication(sys.argv)
 
window = QPushButton("Push Me")
window.show()
 
app.exec()
"""
 
#Example 3. Use QMainWindow generic object instead.
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
 
app = QApplication(sys.argv)
 
#A standard window... it is empty now however...
window = QMainWindow()
window.show()
 
# Start the event loop.
app.exec()
"""
 
#Example 4. This is the standard: accessing QMainWindow through a subclass.
"""
import sys
 
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
 
# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
 
        # Set the central widget of the Window.
        self.setCentralWidget(button)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 5. You may access functions, methods and properties of QMainWindow in your own derived class.
"""
import sys
 
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
 
# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        self.setFixedSize(QSize(400, 300))
 
        # Set the central widget of the Window.
        self.setCentralWidget(button)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""

#Examples shamelessly taken from
#https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/
 
#Example 6. The custom object method accepts the clicked signal from the QPushButton.
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        button = QPushButton("Press Me!")
        #set button in toggle (or check) mode
        button.setCheckable(True)
        #do something if the button is pressed
        button.clicked.connect(self.the_button_was_clicked)
 
        # Set the central widget of the Window.
        self.setCentralWidget(button)
 
    def the_button_was_clicked(self):
        print("Clicked!")
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 7. The .clicked signal provides a checked (or toggled) state for the button.
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        #if the button is clicked it will activate the two lines below
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
 
        self.setCentralWidget(button)
 
    def the_button_was_clicked(self):
        print("Clicked!")
 
    def the_button_was_toggled(self, checked):
        print("Checked?", checked)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 8. You can store a state inside the object as an attribute.
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.button_is_checked = True
 
        self.setWindowTitle("My App")
 
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)
 
        self.setCentralWidget(button)
 
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 9. Change the state of the window and button with a click.
'''
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
 
        self.setCentralWidget(self.button)
 
    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)
 
        # Also change the window title.
        self.setWindowTitle("My Oneshot App")
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
'''
 
#Example 10. Change the title of the window until a certain event happens.
'''
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
 
import sys
from random import choice
 
window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.n_times_clicked = 0
 
        self.setWindowTitle("My App")
 
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        
        #.windowTitleChanged is a signal of QMainWindow
        self.windowTitleChanged.connect(self.the_window_title_changed)
 
        # Set the central widget of the Window.
        self.setCentralWidget(self.button)
 
    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)
 
    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
 
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
'''
 
#Example 11. Dynamic input display.
"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
import sys
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
        
        #set as attribute of MainWindow something called label which is a QLabel object
        self.label = QLabel()
        
        #set as another attribute of MainWindow something called input which is a QLineEdit prompt
        self.input = QLineEdit()
        #if the signal textChanged is sent from input, the do: to the label, set its text
        self.input.textChanged.connect(self.label.setText)
        
        #instead of making an array, call the QVBoxLayout to handle presentation for you
        layout = QVBoxLayout()
        #add the two widgets to your layout
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        
        #now make a widget with that layout
        container = QWidget()
        container.setLayout(layout)
 
        # and set it as the central widget of the window
        self.setCentralWidget(container)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 12. Mouse events.
"""
import sys
 
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
 
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
 
    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")
 
    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")
 
    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 13. Specific mouse events.
"""
import sys
 
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
 
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
 
    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")
 
    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")
 
    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")
 
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")
 
        elif e.button() == Qt.MouseButton.MiddleButton:
            # handle the middle-button press in here.
            self.label.setText("mousePressEvent MIDDLE")
 
        elif e.button() == Qt.MouseButton.RightButton:
            # handle the right-button press in here.
            self.label.setText("mousePressEvent RIGHT")
 
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")
 
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")
 
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")
 
    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")
 
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")
 
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
'''
#Example 14. Context menus.

import sys
 
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
'''
 
