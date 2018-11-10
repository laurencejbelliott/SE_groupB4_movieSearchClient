# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt4 UI code generator 4.11.4

from datetime import date
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

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
        MainWindow.resize(782, 406)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mainVLayout = QtGui.QVBoxLayout()
        self.mainVLayout.setObjectName(_fromUtf8("mainVLayout"))
        self.searchBarHLayout = QtGui.QHBoxLayout()
        self.searchBarHLayout.setObjectName(_fromUtf8("searchBarHLayout"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.searchBarHLayout.addWidget(self.lineEdit)
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setMinimumSize(QtCore.QSize(93, 28))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.searchBarHLayout.addWidget(self.searchButton)
        self.mainVLayout.addLayout(self.searchBarHLayout)
        self.searchOptionsHLayout = QtGui.QHBoxLayout()
        self.searchOptionsHLayout.setObjectName(_fromUtf8("searchOptionsHLayout"))
        self.yearVLayout = QtGui.QVBoxLayout()
        self.yearVLayout.setObjectName(_fromUtf8("yearVLayout"))
        self.yearLabel = QtGui.QLabel(self.centralwidget)
        self.yearLabel.setObjectName(_fromUtf8("yearLabel"))
        self.yearVLayout.addWidget(self.yearLabel)
        self.yearChoiceBox = QtGui.QComboBox(self.centralwidget)
        self.yearChoiceBox.setObjectName(_fromUtf8("yearChoiceBox"))
        self.yearVLayout.addWidget(self.yearChoiceBox)
        self.searchOptionsHLayout.addLayout(self.yearVLayout)
        self.dateHLayout = QtGui.QHBoxLayout()
        self.dateHLayout.setObjectName(_fromUtf8("dateHLayout"))
        self.dateVLayout = QtGui.QVBoxLayout()
        self.dateVLayout.setObjectName(_fromUtf8("dateVLayout"))
        self.dateLabelEnableHLayout = QtGui.QHBoxLayout()
        self.dateLabelEnableHLayout.setObjectName(_fromUtf8("dateLabelEnableHLayout"))
        self.dateLabel = QtGui.QLabel(self.centralwidget)
        self.dateLabel.setEnabled(False)
        self.dateLabel.setObjectName(_fromUtf8("dateLabel"))
        self.dateLabelEnableHLayout.addWidget(self.dateLabel)
        self.dateEnableBox = QtGui.QCheckBox(self.centralwidget)
        self.dateEnableBox.setText(_fromUtf8(""))
        self.dateEnableBox.setObjectName(_fromUtf8("dateEnableBox"))
        self.dateLabelEnableHLayout.addWidget(self.dateEnableBox)
        self.dateVLayout.addLayout(self.dateLabelEnableHLayout)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setEnabled(False)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateVLayout.addWidget(self.dateEdit)
        self.dateHLayout.addLayout(self.dateVLayout)
        self.apiVLayout = QtGui.QVBoxLayout()
        self.apiVLayout.setObjectName(_fromUtf8("apiVLayout"))
        self.apiLabel = QtGui.QLabel(self.centralwidget)
        self.apiLabel.setObjectName(_fromUtf8("apiLabel"))
        self.apiVLayout.addWidget(self.apiLabel)
        self.apiChoiceBox = QtGui.QComboBox(self.centralwidget)
        self.apiChoiceBox.setObjectName(_fromUtf8("apiChoiceBox"))
        self.apiChoiceBox.addItem(_fromUtf8(""))
        self.apiChoiceBox.addItem(_fromUtf8(""))
        self.apiVLayout.addWidget(self.apiChoiceBox)
        self.dateHLayout.addLayout(self.apiVLayout)
        self.searchOptionsHLayout.addLayout(self.dateHLayout)
        self.mainVLayout.addLayout(self.searchOptionsHLayout)
        self.verticalLayout.addLayout(self.mainVLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
        curYear = date.today().year
        yearOptions = [year for year in range(curYear+4, 1849, -1)]

        yearCount = 0
        for year in yearOptions:
             self.yearChoiceBox.addItem(_fromUtf8(""))
             self.yearChoiceBox.setItemText(yearCount, _translate("MainWindow", str(year), None))
             yearCount += 1   

        self.resultWindows = []

        self.dateEnableBox.toggled.connect(lambda:self.toggleDate(self.dateEnableBox))
        self.searchButton.clicked.connect(self.showResults)
        self.actionQuit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        MainWindow.closeEvent = self.closeEvent

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Information - Search", None))
        self.lineEdit.setText(_translate("MainWindow", "Search for movie by title or IMDB number", None))
        self.searchButton.setText(_translate("MainWindow", "Go", None))
        self.yearLabel.setText(_translate("MainWindow", "Year", None))


        self.dateLabel.setText(_translate("MainWindow", "Date", None))
        self.apiLabel.setText(_translate("MainWindow", "API", None))
        self.apiChoiceBox.setItemText(0, _translate("MainWindow", "TMDb", None))
        self.apiChoiceBox.setItemText(1, _translate("MainWindow", "OMDB", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
	
    def toggleDate(self, dateEnableBox):
        checked = dateEnableBox.isChecked()
        
        self.dateLabel.setEnabled(checked)
        self.dateEdit.setEnabled(checked)
        self.yearLabel.setEnabled(not checked)
        self.yearChoiceBox.setEnabled(not checked)

    def showResults(self):
        self.resultWindows.append(Ui_ResultsWindow())

    def closeEvent(self, event):        
        sys.exit(app.exec_())



class Ui_ResultsWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_ResultsWindow, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Results for <search text>")
        resultsWidget = QtGui.QWidget(self)
        self.setCentralWidget(resultsWidget)
        gridLayout = QVBoxLayout()
        resultsWidget.setLayout(gridLayout)
        resultsTextBox = QTextEdit()
        resultsHTML = """
<b>Die Hard (1998)</b>
<br>
Released (Release placeholder)
<br>
Rated M
<br><br>
<b>Length</b>
<br>
(Length placeholder)
<br><br>
<b>Genre</b>
<br>
Action
<br>Long text long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text text long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text text long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text  long text
"""
        resultsTextBox.setHtml(resultsHTML)
        resultsTextBox.setReadOnly(True)
        resultsScroll = QtGui.QScrollArea()
        resultsScroll.setWidget(resultsTextBox)
        resultsScroll.setWidgetResizable(True)
        gridLayout.addWidget(resultsScroll)

        self.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())