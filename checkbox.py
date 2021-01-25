from PySide2.QtWidgets import QApplication,QMainWindow,QFontComboBox,QGroupBox,QGridLayout,QStatusBar,QDesktopWidget,QWidget,QVBoxLayout,QLabel,QCheckBox
from PySide2.QtGui import  QIcon,QFont
from PySide2.QtCore import Qt
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My App')
        self.setGeometry(100,100,500,500)
        self.widget = widget(self)
        self.setCentralWidget(self.widget)
        self.setIcon()
        self.center()
        self.Makebar('App ready',3000)
    def setIcon(self):
        ic = QIcon('download.jpeg')
        self.setWindowIcon(ic)
    def Makebar(self,msg,dur):
        bar = QStatusBar()
        bar.showMessage(msg,dur)
        self.setStatusBar(bar)
    def center(self):
        f = self.frameGeometry()
        center = QDesktopWidget().frameGeometry().center()
        f.moveCenter(center)
        self.move(f.topLeft())
class widget(QWidget):
    def __init__(self,parent = None):
        super(widget, self).__init__(parent)
        self.createcheckbox()
    def createcheckbox(self):
        vbox = QVBoxLayout()
        group = QGroupBox('Which Game do you like')
        group.setFont(QFont('Sanserif', 13))
        grid = QGridLayout()
        self.l = QLabel('',self)
        check = QCheckBox('FootBall',self)
        check.stateChanged.connect(self.checkclik)
        grid.addWidget(check,0,0)

        grid.addWidget(self.l,3,0)
        font = QFontComboBox()
        font.setFontFilters(QFontComboBox.MonospacedFonts)
        grid.addWidget(font,4,0)
        group.setLayout(grid)
        vbox.addWidget(group)
        self.setLayout(vbox)
    def checkclik(self,state):
        if state == Qt.Checked:
            self.l.setText('I like Football')
        else:
            self.l.setText("I don't like Football")

MyApp = QApplication(sys.argv)
win = MainWindow()
win.show()
MyApp.exec_()
sys.exit()