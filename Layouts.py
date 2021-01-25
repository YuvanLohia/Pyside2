from PySide2.QtWidgets import QApplication,QMainWindow,QWidget,QGridLayout,QStatusBar,QDesktopWidget,QGroupBox,QPushButton,QDialog,QVBoxLayout,QHBoxLayout
from PySide2.QtGui import QIcon,QFont
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My App')
        self.form_widget = grid(self)

        self.form_widget.setGeometry(0,0,500,200)

        self.setGeometry(100,100,500,500)
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

class VboxandHbox(QWidget):
    def __init__(self,parent =None):
        super(VboxandHbox, self).__init__(parent)

        self.createlayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.group)
        self.setLayout(vbox)




    def createlayout(self):
        self.group = QGroupBox('Plz choose one language')
        self.group.setFont(QFont('Sanserif',13))
        hbox = QHBoxLayout()
        b1 = QPushButton('CSS',self)
        b1.setMinimumHeight(40)
        hbox.addWidget(b1)
        b2 = QPushButton('Java',self)
        b2.setMinimumHeight(40)
        hbox.addWidget(b2)
        b3 = QPushButton('Python',self)
        b3.setMinimumHeight(40)
        hbox.addWidget(b3)
        self.group.setLayout(hbox)
class grid(QWidget):
    def __init__(self,parent = None):
        super(grid, self).__init__(parent)

        self.creategrid()
        vbox = QVBoxLayout()
        vbox.addWidget(self.group)
        self.setLayout(vbox)
    def creategrid(self):
        self.group = QGroupBox('Plz choose one language')
        self.group.setFont(QFont('Sanserif', 13))
        grid = QGridLayout()
        b1 = QPushButton('CSS', self)
        b1.setMinimumHeight(40)
        grid.addWidget(b1,0,0)
        b2 = QPushButton('Java', self)
        b2.setMinimumHeight(40)
        grid.addWidget(b2,1,1)
        b3 = QPushButton('Python', self)
        b3.setMinimumHeight(40)
        grid.addWidget(b3,2,2)
        self.group.setLayout(grid)
MyApp = QApplication(sys.argv)
win = MainWindow()
win.show()
MyApp.exec_()
sys.exit()