from PySide2.QtWidgets import QApplication,QDialog,QProgressBar,QStatusBar,QVBoxLayout,QPushButton,QMainWindow
from PySide2.QtWidgets import QDesktopWidget
from PySide2.QtGui import QIcon
import sys,time
from PySide2.QtCore import QThread,Qt,Signal
class Thread(QThread):
    change_va = Signal(int)
    def run(self):
        cnt = 0
        while cnt < 100:
            cnt += 1
            time.sleep(0.3)
            self.change_va.emit(cnt)

class Wi(QDialog):
    def __init__(self):
        super(Wi, self).__init__()
        self.show()
        self.setWindowTitle('Wana run')
        self.setGeometry(100,100,100,100)
        self.center()
        self.setIcon()
        self.pr()

    def setIcon(self):
        i = QIcon('download.jpeg')
        self.setWindowIcon(i)
    def center(self):
        f = self.frameGeometry()
        center = QDesktopWidget().frameGeometry().center()
        f.moveCenter(center)
        self.move(f.topLeft())
    def pr(self):
        v = QVBoxLayout()
        self.prog = QProgressBar()
        v.addWidget(self.prog)
        self.b = QPushButton('Run')
        self.b.clicked.connect(self.start)
        v.addWidget(self.b)
        self.setLayout(v)
    def start(self):
        self.thread = Thread()
        self.thread.change_va.connect(self.va)
        self.thread.start()
    def va(self,v):
        if self.thread.isFinished():
            self.destroy()
        self.prog.setValue(v)

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('My App')
        self.setGeometry(100, 100, 500, 500)
        self.setIcon()
        self.center()
        b = QPushButton('Download ebook',self)
        b.clicked.connect(self.c)
        self.setbar('App Running Perfectly',3000)
    def setIcon(self):
        i = QIcon('download.jpeg')
        self.setWindowIcon(i)

    def center(self):
        f = self.frameGeometry()
        center = QDesktopWidget().frameGeometry().center()  
        f.moveCenter(center)
        self.move(f.topLeft())
    def c(self):
        self.w = Wi()
    def setbar(self,m,v):
        self.bar = QStatusBar()
        self.bar.showMessage(m,v)
        self.setStatusBar(self.bar)
myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit()