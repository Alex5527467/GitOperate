# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alex\TrajectoryCreate\TrajectoryV1\UI_Maindow.ui'
#
# Created: Wed Mar 28 13:29:53 2018
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from window1 import StatWindow

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_F = QtGui.QMenu(self.menubar)
        self.menu_F.setObjectName(_fromUtf8("menu_F"))
        self.menu_O = QtGui.QMenu(self.menubar)
        self.menu_O.setObjectName(_fromUtf8("menu_O"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionTest1 = QtGui.QAction(MainWindow)
        self.actionTest1.setObjectName(_fromUtf8("actionTest1"))
        self.actionTest2 = QtGui.QAction(MainWindow)
        self.actionTest2.setObjectName(_fromUtf8("actionTest2"))
        self.actionTest3 = QtGui.QAction(MainWindow)
        self.actionTest3.setObjectName(_fromUtf8("actionTest3"))
        self.menu_O.addAction(self.actionTest1)
        self.menu_O.addAction(self.actionTest2)
        self.menu_O.addAction(self.actionTest3)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_O.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionTest1.triggered.connect(self.on_actionTest1_activated)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu_F.setTitle(_translate("MainWindow", "文件(F)", None))
        self.menu_O.setTitle(_translate("MainWindow", "操作(O)", None))
        self.actionTest1.setText(_translate("MainWindow", "Test1", None))
        self.actionTest2.setText(_translate("MainWindow", "Test2", None))
        self.actionTest3.setText(_translate("MainWindow", "Test3", None))

    def on_actionTest1_activated(self):
        statwindow = StatWindow(self)
        statwindow.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

