from ui.test_main import MyApp
from ui.table import Table
import PyQt5.QtWidgets as qt
import sys

if __name__ == '__main__':
   app = qt.QApplication(sys.argv)
   ex = MyApp()
   ex2 = Table()
   sys.exit(app.exec_())

