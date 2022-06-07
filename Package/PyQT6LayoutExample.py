#Examples shamelessly taken from
#https://www.pythonguis.com/tutorials/pyqt6-widgets/
 
#Example 23.
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPalette, QColor
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My App")
 
        #make a Color widget (look at the definition below)
        widget = Color('red')
        self.setCentralWidget(widget)
 
class Color(QWidget):
 
    def __init__(self, color):
        #Color object is a type of Widget and turns on the inherited option to auto-fill background
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
 
        #make palette a Color object attribute, then set its color as the given argument
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 24. Vertical Box of Color widgets.
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My App")
 
        layout = QVBoxLayout()
 
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
 
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
 
class Color(QWidget):
 
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
 
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 25. Horizontal box of color widgets.
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from PyQt6.QtGui import QPalette, QColor
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My App")
 
        layout = QHBoxLayout()
 
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
 
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
 
class Color(QWidget):
 
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
 
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 26. Nesting layouts.
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My App")
 
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
 
        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))
 
        layout1.addLayout( layout2 )
 
        layout1.addWidget(Color('green'))
 
        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))
 
        layout1.addLayout( layout3 )
 
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
 
class Color(QWidget):
 
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
 
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 27. Borderless edition.
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My App")
 
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
 
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(20)
 
        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))
 
        layout1.addLayout( layout2 )
 
        layout1.addWidget(Color('green'))
 
        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))
 
        layout1.addLayout( layout3 )
 
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
 
class Color(QWidget):
 
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
 
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 28. A GridLayout widget makes things easier.
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt6.QtGui import QPalette, QColor
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My App")
 
        layout = QGridLayout()
 
        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)
 
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
 
class Color(QWidget):
 
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
 
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 29. Now with buttons.
"""
import sys
 
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()
 
        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)
 
        btn = QPushButton("red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("red"))
 
        btn = QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("green"))
 
        btn = QPushButton("yellow")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("yellow"))
 
        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)
 
    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)
 
    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)
 
    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)
 
class Color(QWidget):
 
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
 
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""
 
#Example 30. The same idea but using QTabWidget.
"""
import sys
 
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
)
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        tabs = QTabWidget()
        tabs.setMovable(True)
 
        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)
 
        self.setCentralWidget(tabs)
 
class Color(QWidget):
 
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
 
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
"""