from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 340, 261, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button1.setObjectName("button1")
        self.verticalLayout.addWidget(self.button1)
        self.button2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button2.setObjectName("button2")
        self.verticalLayout.addWidget(self.button2)
        self.button3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button3.setObjectName("button3")
        self.verticalLayout.addWidget(self.button3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 190, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.check1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.check1.setObjectName("check1")
        self.horizontalLayout.addWidget(self.check1)
        self.check2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.check2.setObjectName("check2")
        self.horizontalLayout.addWidget(self.check2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu = QtWidgets.QMenuBar(MainWindow)
        self.menu.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menu.setObjectName("menu")
        self.menuTest_UI = QtWidgets.QMenu(self.menu)
        self.menuTest_UI.setObjectName("menuTest_UI")
        MainWindow.setMenuBar(self.menu)
        self.status = QtWidgets.QStatusBar(MainWindow)
        self.status.setObjectName("status")
        MainWindow.setStatusBar(self.status)
        self.menu.addAction(self.menuTest_UI.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "Button 1"))
        self.button2.setText(_translate("MainWindow", "Button 2"))
        self.button3.setText(_translate("MainWindow", "Button 3"))
        self.check1.setText(_translate("MainWindow", "Check 1"))
        self.check2.setText(_translate("MainWindow", "Check 2"))
        self.menuTest_UI.setTitle(_translate("MainWindow", "Test UI "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())