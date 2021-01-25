from PySide2.QtWidgets import QApplication,QLCDNumber,QMainWindow, QStatusBar,QInputDialog, QDesktopWidget, QWidget,QCalendarWidget,QVBoxLayout
from PySide2.QtGui import QIcon,QTextCharFormat,QPalette,Qt
import sys
from PySide2.QtCore import QTimer,QTime,SIGNAL


class DigitalClock(QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)
        self.setGeometry(0,0,100,50)
        self.setSegmentStyle(QLCDNumber.Filled)
        timer = QTimer(self)
        self.connect(timer, SIGNAL('timeout()'), self.shoe)
        timer.start(1000)
        self.shoe()

    def shoe(self):

        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My App')
        self.setGeometry(100, 100, 500, 500)
        self.widget = widget(self)
        self.timer = DigitalClock(self)
        self.timer.move(400,0)
        self.widget.move(0,50)
        self.setIcon()
        self.center()
        self.Makebar('App ready', 3000)

    def setIcon(self):
        ic = QIcon('download.jpeg')
        self.setWindowIcon(ic)

    def Makebar(self, msg, dur):
        bar = QStatusBar()
        bar.showMessage(msg, dur)
        self.setStatusBar(bar)

    def center(self):
        f = self.frameGeometry()
        center = QDesktopWidget().frameGeometry().center()
        f.moveCenter(center)
        self.move(f.topLeft())


class widget(QWidget):
    def __init__(self, parent=None):
        super(widget, self).__init__(parent)
        self.setGeometry(0,0,500,300)
        self.createcalender()
        self.highlight_format = QTextCharFormat()
        self.highlight_format.setBackground(Qt.red)
        self.highlight_format.setForeground(self.palette().color(QPalette.HighlightedText))
    def createcalender(self):
        vbox = QVBoxLayout()
        self.cal = QCalendarWidget()
        vbox.addWidget(self.cal)
        self.cal.selectionChanged.connect(self.paint)
        self.setLayout(vbox)
    def paint(self):
        text, ok = QInputDialog.getText(self, 'Set Event', 'Enter event title:')

        if ok:
            self.cal.setDateTextFormat(self.cal.selectedDate(),self.highlight_format)

MyApp = QApplication(sys.argv)
win = MainWindow()
win.show()
MyApp.exec_()
sys.exit()
