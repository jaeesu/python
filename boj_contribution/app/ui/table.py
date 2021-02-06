import sys
import PyQt5.QtWidgets as qt

class Table(qt.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('contribution_Table')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__=='__main__':
    app = qt.QApplication(sys.argv)
    ex = Table()
    sys.exit(app.exec_())
