#!/usr/bin/env python3


from MainWindow import *                                                                                                         #never tamper with the other file, use import to call everything here!!


def signals(self):
    self.lineEdit1.textEdited['QString'].connect(self.calc)                                                                      #signals for connecting all the GUI object to functions
    self.lineEdit1.textEdited['QString'].connect(self.calc)
    self.pushButton.clicked.connect(self.calc)
    self.pushButton2.clicked.connect(self.clear)
    self.comboBox1.activated[str].connect(self.calc)
    self.comboBox2.activated[str].connect(self.calc)
    self.comboBox2.activated[str].connect(self.calc)
    self.comboBox2.activated[str].connect(self.calc)

    colorCodes = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White']                       # Created a list for the codes
    tolCodes = ['Gold', 'Silver']

    for color in colorCodes:                                                                                                    # for loop to create the comboBoxes using above list
        self.comboBox1.addItem(color)
        self.comboBox2.addItem(color)
        self.comboBox3.addItem(color)

    for tol in tolCodes:
        self.comboBox4.addItem(tol)

def clear(self):
    clean = ''
    self.lineEdit1.setText(clean)                                                                                                 #assigns the value to the lineEdit(may change to LED in future)
    self.lineEdit2.setText(clean)

def calc(self):
    cb1 = self.comboBox1.currentText()                                                                                           #assigned the current value of each comboBox to a variable
    cb2 = self.comboBox2.currentText()
    cb3 = self.comboBox3.currentText()
    cb4 = self.comboBox4.currentText()

    codeDict = {'Black': 0, 'Brown': 1, 'Red':2, 'Orange':3, 'Yellow':4, 'Green':5, 'Blue':6, 'Violet':7, 'Grey':8, 'White':9}   #Created a dictionary for value assignment(Better tha an if-elif ladder)
    tolDict = {'Gold':5, 'Silver':10}
    ohm = float(((codeDict[cb1]*10)+codeDict[cb2])*(10**codeDict[cb3]))                                                          #HECK YEAH! FINALLY!
    kOhm = str(ohm/1000)
    tol = str(tolDict[cb4])
    self.lineEdit1.setText(kOhm)                                                                                                 #assigns the value to the lineEdit(may change to LED in future)
    self.lineEdit2.setText(tol)




Ui_MainWindow.signals = signals                                                                                                 # add all the new functions to Ui_MainWindow
Ui_MainWindow.calc = calc
Ui_MainWindow.clear = clear

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()                                                                                                                #added this to make sure everything is linked
    MainWindow.show()
    sys.exit(app.exec_())
