# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(650, 277)
        MainWindow.setMinimumSize(QtCore.QSize(650, 277))
        MainWindow.setMaximumSize(QtCore.QSize(650, 277))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lightning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(160, 30, 211, 31))
        self.comboBox1.setObjectName("comboBox1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(16)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 50, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(10)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(610, 140, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 180, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(390, 50, 211, 41))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(390, 130, 211, 41))
        self.lineEdit2.setObjectName("lineEdit2")
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(160, 80, 211, 31))
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox3.setGeometry(QtCore.QRect(160, 130, 211, 31))
        self.comboBox3.setObjectName("comboBox3")
        self.comboBox4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox4.setGeometry(QtCore.QRect(160, 180, 211, 31))
        self.comboBox4.setObjectName("comboBox4")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(510, 180, 91, 41))
        self.pushButton2.setObjectName("pushButton2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 650, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFIle = QtWidgets.QMenu(self.menuBar)
        self.menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(self.menuBar)
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuFIle.addAction(self.actionExit_2)
        self.menuBar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit_2.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resistance Calculator"))
        self.comboBox1.setToolTip(_translate("MainWindow", "Enter color of first band"))
        self.comboBox1.setStatusTip(_translate("MainWindow", "Enter color of first band"))
        self.label.setText(_translate("MainWindow", "First Band"))
        self.label_2.setText(_translate("MainWindow", "Second Band"))
        self.label_3.setText(_translate("MainWindow", "Third Band"))
        self.label_4.setText(_translate("MainWindow", "Fourth Band"))
        self.label_6.setText(_translate("MainWindow", "Resistance Value is :"))
        self.label_7.setText(_translate("MainWindow", " kΩ"))
        self.label_8.setText(_translate("MainWindow", "Tolerance(+/-) :"))
        self.label_9.setText(_translate("MainWindow", "%"))
        self.pushButton.setToolTip(_translate("MainWindow", "Calculate"))
        self.pushButton.setStatusTip(_translate("MainWindow", "Find Value"))
        self.pushButton.setText(_translate("MainWindow", "Calculate !"))
        self.lineEdit1.setToolTip(_translate("MainWindow", "Resistance Value"))
        self.lineEdit1.setStatusTip(_translate("MainWindow", "Resistance Value"))
        self.lineEdit2.setToolTip(_translate("MainWindow", "Tolerance"))
        self.lineEdit2.setStatusTip(_translate("MainWindow", "Tolerance"))
        self.comboBox2.setToolTip(_translate("MainWindow", "Enter color of second band"))
        self.comboBox2.setStatusTip(_translate("MainWindow", "Enter color of second band"))
        self.comboBox3.setToolTip(_translate("MainWindow", "Enter color of second band"))
        self.comboBox3.setStatusTip(_translate("MainWindow", "Enter color of second band"))
        self.comboBox4.setToolTip(_translate("MainWindow", "Enter color of first band"))
        self.comboBox4.setStatusTip(_translate("MainWindow", "Enter color of first band"))
        self.pushButton2.setToolTip(_translate("MainWindow", "Clear"))
        self.pushButton2.setStatusTip(_translate("MainWindow", "Clear Boxes"))
        self.pushButton2.setText(_translate("MainWindow", "Clear"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionExit_2.setStatusTip(_translate("MainWindow", "Exit the application"))
        self.actionExit_2.setShortcut(_translate("MainWindow", "Ctrl+X"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

