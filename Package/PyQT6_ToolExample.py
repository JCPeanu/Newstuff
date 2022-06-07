#Examples shamelessly taken from
#https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/
 
#Example 31. An empty toolbar.
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My Awesome App")
 
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        self.setCentralWidget(label)
 
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
 
    def onMyToolBarButtonClick(self, s):
        print("click", s)
 
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
"""
 
#Example 32. Now with a button.
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My Awesome App")
 
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        self.setCentralWidget(label)
 
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        
        #QAction is a class that provides a way to describe abstract user interfaces.
        #Meaning you can define multiple interface elements within a single object, 
        #unified by the effect that interacting with that element has. 
        
        #define a single QAction, defining the triggered action, 
        #and then add this action to both the menu and the toolbar. 
        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)
 
    def onMyToolBarButtonClick(self, s):
        print("click", s)
 
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
"""
 
#Example 33.
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My Awesome App")
 
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        self.setCentralWidget(label)
 
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
 
        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)
 
        self.setStatusBar(QStatusBar(self))
 
    def onMyToolBarButtonClick(self, s):
        print("click", s)
 
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
"""
 
#Example 34
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My Awesome App")
 
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        self.setCentralWidget(label)
 
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
 
        button_action = QAction("Your button!", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
 
        self.setStatusBar(QStatusBar(self))
 
    def onMyToolBarButtonClick(self, s):
        print("click", s)
 
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
"""
 
#Example 35
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle("My Awesome App")
 
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        self.setCentralWidget(label)
 
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
 
        #https://p.yusukekamiyamane.com/ <- lots of free icons, royalty-free
        button_action = QAction(QIcon("Rock.webp"), "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
 
        self.setStatusBar(QStatusBar(self))
 
    def onMyToolBarButtonClick(self, s):
        print("click", s)
 
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
"""
 
#Example 36
'''
import sys
 
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        self.setCentralWidget(label)
 
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
 
        button_action = QAction(QIcon("RockNew.jpg"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
 
        toolbar.addSeparator()
 
        button_action2 = QAction(QIcon("Paper.jpeg"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
 
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
 
        self.setStatusBar(QStatusBar(self))
 
    def onMyToolBarButtonClick(self, s):
        print("click", s)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
'''
 
#Example 37
'''
import sys
 
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        self.setCentralWidget(label)
 
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
 
        button_action = QAction(QIcon("Paper.jpeg"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
 
        toolbar.addSeparator()
 
        button_action2 = QAction(QIcon("Rock.webp"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
 
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
 
        self.setStatusBar(QStatusBar(self))
 
        menu = self.menuBar()
 
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
 
    def onMyToolBarButtonClick(self, s):
        print("click", s)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
'''
 
#Example 38
'''
import sys
 
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        self.setCentralWidget(label)
 
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
 
        button_action = QAction(QIcon("Paper.jpeg"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
 
        toolbar.addSeparator()
 
        button_action2 = QAction(QIcon("RockNew.jpg"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
 
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
 
        self.setStatusBar(QStatusBar(self))
 
        menu = self.menuBar()
 
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)
 
    def onMyToolBarButtonClick(self, s):
        print("click", s)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
'''
 
#Example 39
'''
import sys
 
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        self.setCentralWidget(label)
 
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
 
        button_action = QAction(QIcon("Paper.jpeg"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
 
        toolbar.addSeparator()
 
        button_action2 = QAction(QIcon("RockNew.jpg"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
 
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
 
        self.setStatusBar(QStatusBar(self))
 
        menu = self.menuBar()
 
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
 
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)
 
    def onMyToolBarButtonClick(self, s):
        print("click", s)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
'''
 
#Example 40
'''
import sys
 
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("My App")
 
        label = QLabel("Hello!")
 
        # The `Qt` namespace has a lot of attributes to customize
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)
 
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
 
        button_action = QAction(QIcon("Paper.jpeg"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        # You can enter keyboard shortcuts using key names (e.g. Ctrl+p)
        # Qt.namespace identifiers (e.g. Qt.CTRL + Qt.Key_P)
        # or system agnostic identifiers (e.g. QKeySequence.Print)
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        toolbar.addAction(button_action)
 
        toolbar.addSeparator()
 
        button_action2 = QAction(QIcon("RockNew.jpg"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action)
 
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
 
        self.setStatusBar(QStatusBar(self))
 
        menu = self.menuBar()
 
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
 
        file_menu.addSeparator()
 
        file_submenu = file_menu.addMenu("Submenu")
 
        file_submenu.addAction(button_action2)
 
    def onMyToolBarButtonClick(self, s):
        print("click", s)
 
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()
'''