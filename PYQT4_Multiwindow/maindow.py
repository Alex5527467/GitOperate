# -*- coding: utf-8 -*-

import os
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *


from UI_Maindow import *
from window1 import StatWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    PyGrid's main window
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainForm = MainWindow()
    mainForm.show()
    sys.exit(app.exec_())
