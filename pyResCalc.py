# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(630, 240)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.comboBox1 = QtGui.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(140, 30, 211, 31))
        self.comboBox1.setObjectName(_fromUtf8("comboBox1"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Serif"))
        font.setPointSize(16)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(590, 50, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(10)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(590, 140, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 180, 201, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(370, 50, 211, 41))
        self.lineEdit1.setObjectName(_fromUtf8("lineEdit1"))
        self.lineEdit2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(370, 130, 211, 41))
        self.lineEdit2.setObjectName(_fromUtf8("lineEdit2"))
        self.comboBox2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(140, 80, 211, 31))
        self.comboBox2.setObjectName(_fromUtf8("comboBox2"))
        self.comboBox3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox3.setGeometry(QtCore.QRect(140, 130, 211, 31))
        self.comboBox3.setObjectName(_fromUtf8("comboBox3"))
        self.comboBox4 = QtGui.QComboBox(self.centralwidget)
        self.comboBox4.setGeometry(QtCore.QRect(140, 180, 211, 31))
        self.comboBox4.setObjectName(_fromUtf8("comboBox4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Resistance Calculator", None))
        self.comboBox1.setToolTip(_translate("MainWindow", "Enter color of first band", None))
        self.comboBox1.setStatusTip(_translate("MainWindow", "Enter color of first band", None))
        self.label.setText(_translate("MainWindow", "First Band", None))
        self.label_2.setText(_translate("MainWindow", "Second Band", None))
        self.label_3.setText(_translate("MainWindow", "Third band", None))
        self.label_4.setText(_translate("MainWindow", "Fourth Band", None))
        self.label_6.setText(_translate("MainWindow", "Resistance Value is :", None))
        self.label_7.setText(_translate("MainWindow", " kΩ", None))
        self.label_8.setText(_translate("MainWindow", "Tolerance(+/-) :", None))
        self.label_9.setText(_translate("MainWindow", "%", None))
        self.pushButton.setToolTip(_translate("MainWindow", "Calculate", None))
        self.pushButton.setStatusTip(_translate("MainWindow", "Find Value", None))
        self.pushButton.setText(_translate("MainWindow", "Calculate !", None))
        self.lineEdit1.setToolTip(_translate("MainWindow", "Resistance Value", None))
        self.lineEdit1.setStatusTip(_translate("MainWindow", "Resistance Value", None))
        self.lineEdit2.setToolTip(_translate("MainWindow", "Tolerance", None))
        self.lineEdit2.setStatusTip(_translate("MainWindow", "Tolerance", None))
        self.comboBox2.setToolTip(_translate("MainWindow", "Enter color of second band", None))
        self.comboBox2.setStatusTip(_translate("MainWindow", "Enter color of second band", None))
        self.comboBox3.setToolTip(_translate("MainWindow", "Enter color of second band", None))
        self.comboBox3.setStatusTip(_translate("MainWindow", "Enter color of second band", None))
        self.comboBox4.setToolTip(_translate("MainWindow", "Enter color of first band", None))
        self.comboBox4.setStatusTip(_translate("MainWindow", "Enter color of first band", None))
        self.actionClear.setText(_translate("MainWindow", "Clear", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
