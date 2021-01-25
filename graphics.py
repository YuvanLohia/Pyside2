from PySide2.QtWidgets import *
from PySide2.QtGui import  QIcon,QBrush,QPen
from PySide2.QtCore import Qt
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My App')
        self.setGeometry(100,100,500,500)


        self.setIcon()
        self.center()
        self.Makebar('App ready',3000)
        self.create_ui()
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
    def create_ui(self):
        scene  = QGraphicsScene(self)
        green = QBrush(Qt.green)
        red = QBrush(Qt.red)
        blue = QBrush(Qt.blue)
        black =QPen(Qt.black)
        black.setWidth(5)
        el  =  scene.addEllipse(10,10,300,300,black,red)
        rec = scene.addRect(10,10,300,100,black,blue)
        el.setFlag(QGraphicsItem.ItemIsMovable)
        self.view = QGraphicsView(scene,self)
        self.view.setGeometry(0,0,500,500)

MyApp = QApplication(sys.argv)
win = MainWindow()
win.show()
MyApp.exec_()
sys.exit()