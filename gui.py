
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self):
        self.frames = dict()
        self.num = 1
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1361, 679)
        self.save_brt = QtWidgets.QPushButton(Form)
        self.save_brt.setGeometry(QtCore.QRect(1260, 10, 91, 41))
        self.save_brt.clicked.connect(self.test)
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.save_brt.setFont(font)
        self.save_brt.setObjectName("save_brt")
        self.input_user = QtWidgets.QLineEdit(Form)
        self.input_user.setGeometry(QtCore.QRect(1050, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(20)
        self.input_user.setFont(font)
        self.input_user.setObjectName("input_user")
        self.label_txt = QtWidgets.QLabel(Form)
        self.label_txt.setGeometry(QtCore.QRect(1050, 120, 301, 161))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(20)
        self.label_txt.setFont(font)
        self.label_txt.setObjectName("label_txt")
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.save_brt.setText(_translate("Form", "출석"))
        self.label_txt.setText(_translate("Form", "TextLabel"))
    
    def test(self):
        self.frames[f"{self.num}"] = QtWidgets.QFrame(Form)
        self.frames[f"{self.num}"].setGeometry(QtCore.QRect(10 + (self.num - 1) * 36, 10 , 31 , 31))
        self.frames[f"{self.num}"].setFrameShape(QtWidgets.QFrame.Box) 
        self.frames[f"{self.num}"].setFrameShadow(QtWidgets.QFrame.Plain)
        self.frames[f"{self.num}"].setLineWidth(5)
        self.frames[f"{self.num}"].setObjectName("frame")
        self.frames[f"{self.num}"].show()
        self.num = self.num + 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
