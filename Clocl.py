from PySide2.QtWidgets import QApplication,QMainWindow,QStatusBar,QDesktopWidget,QWidget,QLCDNumber,QVBoxLayout
from PySide2.QtCore import QTime,QTimer
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My App')
        self.setGeometry(100,100,200,100)
        self.widget = widget(self)
        self.setCentralWidget(self.widget)

        self.center()
        self.Makebar('App ready',3000)

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

        timer = QTimer(self)
        timer.timeout.connect(self.show_clock)
        timer.start(1000)
        self.show_clock()
    def show_clock(self):
        vbox = QVBoxLayout()
        lcd = QLCDNumber()
        lcd.setStyleSheet('color:green')
        lcd.setStyleSheet('background:yellow')
        vbox.addWidget(lcd)
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        lcd.display(text)
        self.setLayout(vbox)

MyApp = QApplication(sys.argv)
win = MainWindow()
win.show()
MyApp.exec_()
sys.exit()