from PySide2.QtWidgets import *
from PySide2.QtGui import  QIcon,QFont
from PySide2.QtPrintSupport import QPrinter,QPrintPreviewDialog,QPrintDialog
import sys
class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.setWindowTitle('My Notepad App')

        self.setGeometry(100,                       100,500,500)
        self.fname = ''
        self.size = 0
        self.text = QTextEdit(self)
        self.font = QFontComboBox(self)
        self.font.setFontFilters(QFontComboBox.MonospacedFonts)
        self.font.move(10,30)
        self.font.currentFontChanged.connect(self.g)
        self.cb = QComboBox(self)
        self.cb.addItems([str(i) for i in range(5,101,5)])
        self.cb.currentIndexChanged.connect(self.f)

        self.cb.move(200, 25)
        self.text.resize(500,400)
        self.text.move(0,70)
        self.setIcon()
        self.center()
        self.setmenu()
        self.Makebar('App ready',3000)

    def f(self,i):
        self.size = i
        self.text.setFont(QFont(self.font.currentFont().toString().split(',')[0], self.size))
    def g(self):

        print()
        self.text.setFont(QFont(self.font.currentFont().toString().split(',')[0],self.size))

    def setIcon(self):
        self.ic = QIcon('icon.png')
        self.setWindowIcon(self.ic)
    def Makebar(self,msg,dur):
        bar = QStatusBar()
        bar.showMessage(msg,dur)
        self.setStatusBar(bar)
    def center(self):
        f = self.frameGeometry()
        center = QDesktopWidget().frameGeometry().center()
        f.moveCenter(center)
        self.move(f.topLeft())
    def setmenu(self):
        menu = self.menuBar()
        file = menu.addMenu('Files')
        view = menu.addMenu('View')
        edit = menu.addMenu('Edit')
        help = menu.addMenu('Help')
        open = QAction(QIcon("open'.png"),'Open',self)
        open.setShortcut('Ctrl+O')
        exi = QAction(QIcon('exit.png'),'Exit',self)
        exi.setShortcut('esc')
        sav = QAction(QIcon('save.png'),'Save',self)
        sav.setShortcut('Ctrl+S')
        pr = QAction(QIcon('print.png'),'Print Preview',self)
        pr.setShortcut('Ctrl+Shift+P')
        pri = QAction(QIcon('print.png'),'Print',self)
        prdf = QAction(QIcon('pdf.png'),'Export as pdf',self)
        pri.setShortcut('Ctrl+P')
        page = QAction(QIcon('page.png'),'Page',self)
        color = QAction(QIcon('color.png'),'Change Color',self)
        color.setShortcut('Shift+Ctrl+C')
        file.addAction(open)
        file.addAction(sav)
        file.addAction(prdf)
        view.addAction(pr)
        view.addAction(pri)
        view.addAction(page)
        view.addAction(color)
        file.addAction(exi)

        open.triggered.connect(self.open)
        exi.triggered.connect(self.shut)
        pr.triggered.connect(self.p)
        pri.triggered.connect(self.prin)
        sav.triggered.connect(self.save)
        prdf.triggered.connect(self.pdf)
        page.triggered.connect(self.page)
        color.triggered.connect(self.color)
    def open(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            None, "Test Files (*.txt *.doc *.py);; Pdf Files (*.pdf)")
        with open(self.fname[0],'r') as file:
            read= file.read()
        self.text.setText(read)
        self.setWindowTitle(self.fname[0])
    def shut(self):
        inf = QMessageBox().question(self, 'Confirm', 'Do you want to really quit', QMessageBox.Yes | QMessageBox.No)
        if inf == QMessageBox.Yes:
            self.close()
        else:
            pass
    def p(self):
        printer = QPrinter(QPrinter.HighResolution)
        priw = QPrintPreviewDialog(printer,self)
        priw.paintRequested.connect(self.print)
        priw.exec_()
    def prin(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer,self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.print(printer)
    def print(self,printer):
        self.text.print_(printer)
    def save(self):
        if self.fname == '':
            name =QFileDialog.getSaveFileName(self, 'Open file',
                                            None, "Test Files (*.txt *.doc *.py)")
        else:
            name = self.fname
        with open(name[0], 'w') as file:
            file.write(self.text.toPlainText())
        self.setWindowTitle(name[0])
    def pdf(self):
        name = QFileDialog.getSaveFileName(self, 'Open file',
                                           None, "Pdf Files (*.pdf)")
        with open(name[0], 'w') as file:
            file.write(self.text.toPlainText())
    def page(self):
        ok,font = QFontDialog.getFont()
        if ok:
            self.text.setFont(font)
    def color(self):
        color = QColorDialog.getColor()
        self.text.setTextColor(color)
MyApp = QApplication(sys.argv)
win = MainWindow()
win.show()
MyApp.exec_()
sys.exit()