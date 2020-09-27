from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.messagesBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.messagesBrowser.setGeometry(QtCore.QRect(10, 60, 411, 411))
        self.messagesBrowser.setObjectName("messagesBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 490, 341, 71))
        self.textEdit.setObjectName("textEdit")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(370, 500, 51, 51))
        self.sendButton.setObjectName("sendButton")
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(322, 20, 101, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 60, 20))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JustAnotherMessenger"))
        self.label.setText(_translate("MainWindow", "JustAnotherMessenger"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Введите текст..."))
        self.sendButton.setText(_translate("MainWindow", ">"))
        self.label_2.setText(_translate("MainWindow", "Ваше имя:"))
