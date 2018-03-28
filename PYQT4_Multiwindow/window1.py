# -*- coding: utf-8 -*-

import os

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from UI_window1 import Ui_MainWindow

class StatWindow(QMainWindow, Ui_MainWindow):
    """
    PyGrid's main window
    """
    def __init__(self, parent = None):
        super(StatWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainForm = StatWindow()
    mainForm.show();
    sys.exit(app.exec_())
