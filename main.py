from PySide2.QtWidgets import QApplication,QMainWindow,QStatusBar,QDesktopWidget,QWidget
from PySide2.QtGui import  QIcon
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My App')
        self.setGeometry(100,100,500,500)
        self.widget = widget(self)

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
MyApp = QApplication(sys.argv)
win = MainWindow()
win.show()
MyApp.exec_()
sys.exit()