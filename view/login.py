
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def openWindow(self):
        app.hide()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(170, 260, 91, 32))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background-color: rgb(74, 136, 150);")
        self.loginButton.setObjectName("loginButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(300, 260, 91, 32))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.cancelButton.setObjectName("cancelButton")

        self.cancelButton.clicked.connect(self.openWindow)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 130, 300))
        self.label.setStyleSheet("background-color: rgb(105, 105, 105);\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.custoID_label = QtWidgets.QLabel(Dialog)
        self.custoID_label.setGeometry(QtCore.QRect(150, 50, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.custoID_label.setFont(font)
        self.custoID_label.setObjectName("custoID_label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(150, 70, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.custoID_label_2 = QtWidgets.QLabel(Dialog)
        self.custoID_label_2.setGeometry(QtCore.QRect(150, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.custoID_label_2.setFont(font)
        self.custoID_label_2.setObjectName("custoID_label_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(150, 120, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(60, 70, 20, 20))
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet("background-color: rgb(74, 136, 150);\n"
"\n"
"\n"
"")
        self.label_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_12.setLineWidth(2)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(40, 30, 20, 20))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("background-color: rgb(74, 136, 150);\n"
"\n"
"\n"
"")
        self.label_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_11.setLineWidth(2)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(20, 50, 20, 20))
        self.label_18.setAutoFillBackground(False)
        self.label_18.setStyleSheet("background-color: rgb(74, 136, 150);\n"
"\n"
"\n"
"")
        self.label_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_18.setLineWidth(2)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(20, 70, 20, 20))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet("background-color: rgb(74, 136, 150);\n"
"\n"
"\n"
"")
        self.label_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_13.setLineWidth(2)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(60, 30, 20, 20))
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet("background-color: rgb(74, 136, 150);\n"
"\n"
"\n"
"")
        self.label_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_14.setLineWidth(2)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(40, 70, 20, 20))
        self.label_17.setAutoFillBackground(False)
        self.label_17.setStyleSheet("background-color: rgb(74, 136, 150);\n"
"\n"
"\n"
"")
        self.label_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_17.setLineWidth(2)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 30, 20, 20))
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("background-color: rgb(74, 136, 150);\n"
"\n"
"\n"
"")
        self.label_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_10.setLineWidth(2)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(40, 50, 20, 20))
        self.label_15.setAutoFillBackground(False)
        self.label_15.setStyleSheet("background-color: rgb(74, 136, 150);\n"
"\n"
"\n"
"")
        self.label_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_15.setLineWidth(2)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(60, 50, 20, 20))
        self.label_16.setAutoFillBackground(False)
        self.label_16.setStyleSheet("background-color: rgb(74, 136, 150);\n"
"\n"
"\n"
"")
        self.label_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_16.setLineWidth(2)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.custoID_label_3 = QtWidgets.QLabel(Dialog)
        self.custoID_label_3.setGeometry(QtCore.QRect(150, 160, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.custoID_label_3.setFont(font)
        self.custoID_label_3.setObjectName("custoID_label_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 180, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.custoID_label_4 = QtWidgets.QLabel(Dialog)
        self.custoID_label_4.setGeometry(QtCore.QRect(150, 200, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.custoID_label_4.setFont(font)
        self.custoID_label_4.setObjectName("custoID_label_4")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(150, 220, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        self.plainTextEdit_3.setFont(font)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login with PIN"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.label_2.setText(_translate("Dialog", "Login with customerID and PIN"))
        self.custoID_label.setText(_translate("Dialog", "CustomerID"))
        self.custoID_label_2.setText(_translate("Dialog", "PIN"))
        self.custoID_label_3.setText(_translate("Dialog", "Security Question"))
        self.label_3.setText(_translate("Dialog", "get question from sql"))
        self.custoID_label_4.setText(_translate("Dialog", "Answer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())