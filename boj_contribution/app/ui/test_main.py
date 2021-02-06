import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButtion, QVBoxLayout
import PyQt5.QtWidgets as qt

#from request import get_message
from ui.table import Table
from service.SettingResponse import  Response_commit_activity 



class MyApp(qt.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = qt.QLabel(self)
        self.lbl.move(60, 40)

        qle = qt.QLineEdit(self)
        qle.move(10, 100)
        qle.textChanged[str].connect(self.onChaged)
        

        grid = qt.QGridLayout()

        grid.addWidget(qt.QLabel('1'), 0, 0, 1, 1)
        grid.addWidget(qt.QLabel('2'), 1, 0, 1, 1)
        grid.addWidget(qt.QLabel('3'), 0, 1, 1, 1)
        grid.addWidget(qt.QLabel('4'), 1, 1, 1, 1)




        btn1 = qt.QPushButton("&Button1", self)
        btn1.setCheckable(True)
        btn1.toggle()


        self.setWindowTitle('Github_Contribution_Table')
        self.move(300, 300)
        self.resize(1000, 1000)
        self.show()
        self.setLayout(grid)

    def onChaged(self, text):
        #self.lbl.setText(text)
        #self.lbl.adjustSize()
        h_req = get_message()
        h_req.repos(text)
        Response_commit_activity(h_req)




