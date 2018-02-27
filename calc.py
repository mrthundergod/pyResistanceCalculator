from pyResCalc import *


def signals(self):
    self.lineEdit1.textEdited['QString'].connect(self.calc)
    self.lineEdit1.textEdited['QString'].connect(self.calc)
    #self.pushButton.clicked.connect()self.calc)
    self.comboBox1.activated[str].connect(self.calc)
    self.comboBox2.activated[str].connect(self.calc)
    self.comboBox2.activated[str].connect(self.calc)
    self.comboBox2.activated[str].connect(self.calc)

    colorCodes = ['Black', 'Blue', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White']
    tolCodes = ['Gold', 'Silver']
    temp = []

    for color in colorCodes:
        self.comboBox1.addItem(color)
        self.comboBox2.addItem(color)
        self.comboBox3.addItem(color)

    for tol in tolCodes:
        self.comboBox4.addItem(tol)

def calc(self):
    cb1 = self.comboBox1.currentText()
    cb2 = self.comboBox2.currentText()
    cb3 = self.comboBox3.currentText()
    cb4 = self.comboBox4.currentText()

    codeDict = {'Black': 0, 'Brown': 1, 'Red':2, 'Orange':3, 'Yellow':4, 'Green':5, 'Blue':6, 'Violet':7, 'Grey':8, 'White':9}
    tolDict = {'Gold':10, 'Silver':20}
    ohm = float(((codeDict[cb1]*10)+codeDict[cb2])*(10**codeDict[cb3]))
    kOhm = str(ohm/1000)
    tol = str(tolDict[cb4])
    self.lineEdit1.setText(kOhm)
    self.lineEdit2.setText(tol)


Ui_MainWindow.signals = signals
Ui_MainWindow.calc = calc



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())
