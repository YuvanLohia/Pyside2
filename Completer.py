from PySide2.QtWidgets import QApplication,QMainWindow,QStatusBar,QPushButton,QLineEdit,QCompleter,QDesktopWidget,QWidget,QGroupBox,QGridLayout,QVBoxLayout
from PySide2.QtGui import  QIcon
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
        self.autocomple()
        vobx = QVBoxLayout()
        vobx.addWidget(self.group)
        self.setLayout(vobx)
    def autocomple(self):
        self.group = QGroupBox('Choose your liked sport:')
        grid = QGridLayout()
        self.names = ['Football','Cricket','Badminton']
        self.comp = QCompleter(self.names)
        self.comp.activated.connect(self.grt)
        self.line = QLineEdit()
        self.line.setCompleter(self.comp)
        grid.addWidget(self.line,0,0)
        self.group.setLayout(grid)
    def grt(self,v):
        print(v)
MyApp = QApplication(sys.argv)
win = MainWindow()
win.show()
MyApp.exec_()
sys.exit()
