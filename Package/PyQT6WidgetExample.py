#Examples shamelessly taken from
#https://www.pythonguis.com/tutorials/pyqt6-widgets/
 
#Example 15. Lots of widgets visualized.

import sys
 
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
'''
# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Widgets App")
 
        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]
 
        for w in widgets:
            layout.addWidget(w())
 
        widget = QWidget()
        widget.setLayout(layout)
 
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
 
app = QApplication(sys.argv)
window = MainWindow()
window.show()
 
app.exec()
'''
 
#Example 16. QLabel are simple messages.
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt6.QtCore import Qt
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My App")
 
        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
 
        self.setCentralWidget(widget)
 
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
"""
 
#Example 17. Checkboxes.
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QGraphicsPixmapItem
)
from PyQt6.QtCore import Qt
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My App")
 
        widget = QCheckBox()
        widget.setCheckState(Qt.CheckState.Checked)
 
        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)
 
        self.setCentralWidget(widget)
 
    def show_state(self, s):
        print(s == Qt.CheckState.Checked)
        print(s)
 
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
"""
 
#Example 18. ComboBox.
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QGraphicsPixmapItem
)
from PyQt6.QtCore import Qt
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My App")
 
        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])
 
        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
 
        self.setCentralWidget(widget)
 
    def index_changed(self, i): # Not an index, i is a QListItem
        print(i.text())
 
    def text_changed(self, s): # s is a str
        print(s)
 
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
"""
 
#Example 19. LineEdit.
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QGraphicsPixmapItem
)
from PyQt6.QtCore import Qt
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My App")
 
        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")
 
        #widget.setReadOnly(True) # uncomment this to make readonly
 
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
 
        self.setCentralWidget(widget)
 
 
    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")
 
    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())
 
    def text_changed(self, s):
        print("Text changed...")
        print(s)
 
    def text_edited(self, s):
        print("Text edited...")
        print(s)
 
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
"""
 
#Example 20. SpinBox.
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QGraphicsPixmapItem
)
from PyQt6.QtCore import Qt
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        widget = QSpinBox()
        # Or: widget = QDoubleSpinBox()
 
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)
 
        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)  # Or e.g. 0.5 for QDoubleSpinBox
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)
 
        self.setCentralWidget(widget)
 
    def value_changed(self, i):
        print(i)
 
    def value_changed_str(self, s):
        print(s)
 
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
"""
 
#Example 21. Slider.
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QGraphicsPixmapItem
)
from PyQt6.QtCore import Qt
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        widget = QSlider()
 
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)
 
        widget.setSingleStep(3)
 
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
 
        self.setCentralWidget(widget)
 
    def value_changed(self, i):
        print(i)
 
    def slider_position(self, p):
        print("position", p)
 
    def slider_pressed(self):
        print("Pressed!")
 
    def slider_released(self):
        print("Released")
 
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
"""
 
#Example 22. Dial.

import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit, QDial,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QGraphicsPixmapItem
)
from PyQt6.QtCore import Qt
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(0.5)
 
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
 
        self.setCentralWidget(widget)
 
    def value_changed(self, i):
        print(i)
 
    def slider_position(self, p):
        print("position", p)
 
    def slider_pressed(self):
        print("Pressed!")
 
    def slider_released(self):
        print("Released")
 
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
