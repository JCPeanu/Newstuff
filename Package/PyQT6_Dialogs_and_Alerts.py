#Examples shamelessly taken from
#https://www.pythonguis.com/tutorials/pyqt6-dialogs/
 
#Example 41
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
 
    def button_clicked(self, s):
        print("click", s)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 42
"""
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
 
    def button_clicked(self, s):
        print("click", s)
 
        dlg = QDialog(self)
        dlg.setWindowTitle("HELLO!")
        dlg.exec()
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 43
"""
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QDialogButtonBox, QVBoxLayout, QLabel
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
 
    def button_clicked(self, s):
        print("click", s)
 
        dlg = CustomDialog()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")
 
class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("HELLO!")
 
        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
 
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
 
        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 44
"""
import sys
 
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
 
    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        button = dlg.exec()
 
        if button == QMessageBox.StandardButton.Ok:
            print("OK!")
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 45
'''
import sys
 
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
 
    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a question dialog")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
 
        if button == QMessageBox.StandardButton.Yes:
            print("Yes!")
        else:
            print("No!")
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
'''
 
#Example 46
"""
import sys
 
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
 
    def button_clicked(self, s):
 
        button = QMessageBox.question(self, "Question dialog", "The longer message")
 
        if button == QMessageBox.StandardButton.Yes:
            print("Yes!")
        else:
            print("No!")
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 47
"""
import sys
 
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
 
    def button_clicked(self, s):
 
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.NoToAll | QMessageBox.StandardButton.Ignore,
            defaultButton=QMessageBox.StandardButton.Discard,
        )
 
        if button == QMessageBox.StandardButton.Discard:
            print("Discard!")
        elif button == QMessageBox.StandardButton.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 