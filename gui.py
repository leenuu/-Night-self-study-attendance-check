from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from main import attendance

class Ui_Form(object):
    def __init__(self):
        self.att = attendance()
        self.frames = dict()
        self.labels = dict()
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1720, 980)
        self.save_brt = QtWidgets.QPushButton(Form)
        self.save_brt.setGeometry(QtCore.QRect(1560, 10, 91, 41))
        
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.save_brt.setFont(font)
        self.save_brt.setObjectName("save_brt")
        self.input_user = QtWidgets.QLineEdit(Form)
        self.input_user.setGeometry(QtCore.QRect(1350, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.input_user.setFont(font)
        self.input_user.setObjectName("input_user")
        self.label_txt = QtWidgets.QLabel(Form)
        self.label_txt.setGeometry(QtCore.QRect(1350, 120, 301, 161))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.label_txt.setFont(font)
        self.label_txt.setObjectName("label_txt")
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.save_brt.clicked.connect(self.attend)
        self.setup_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.save_brt.setText(_translate("Form", "출석"))
        self.label_txt.setText(_translate("Form", "TextLabel"))

    def attend(self):
        _translate = QtCore.QCoreApplication.translate
        user = str(self.input_user.text())
        print(user)
        try:
            if str(datetime.today().strftime("%Y-%m-%d")) != self.att.data[user]["last_date"] and self.att.data[user]["check_time"] == None:
                self.att.data[user]["last_date"] = str(datetime.today().strftime("%Y-%m-%d"))
                self.att.data[user]["check_time"] = str(datetime.today().strftime("%H:%M:%S")) 
                self.att.data[user]["count"] = self.att.data[user]["count"] + 1
                self.att.schedule_check(user)
                self.label_txt.setText(_translate("Form","출석완료."))
                if self.att.data[user]["second_day"] != ['None'] and len(str(self.att.data[user]["check_time"])) <= 10:
                    self.labels[f"{user}"].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
                elif self.att.data[user]["second_day"] == ['None']:
                    self.labels[f"{user}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")

                print("출석완료.")
                print('\n',end='')

            elif self.att.check_time(self.att.data[user]["check_time"]):
                self.att.data[user]["check_time"] = self.att.data[user]["check_time"] + str(datetime.today().strftime("%H:%M:%S"))
                self.att.schedule_check(user)
                self.labels[f"{user}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
                self.label_txt.setText(_translate("Form","출석완료."))
                print("출석완료.")
                print('\n',end='')
            
            elif str(datetime.today().strftime("%Y-%m-%d")) == self.att.data[user]["last_date"] and self.att.check_time(self.att.data[user]["check_time"]) == False:
                self.label_txt.setText(_translate("Form","이미 출석 하셨습니다."))
                print("이미 춣석 하셨습니다.")
                print('\n',end='')
            

        except KeyError:
            print("keyError")
            pass

        self.input_user.setText("")


    def setup_(self):
        x = 1
        y = 1
        _translate = QtCore.QCoreApplication.translate
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(12)
        font.setBold(True)
        n= 0
        while True:
            print(self.att.users[n])
            self.frames[f"{self.att.users[n]}"] = QtWidgets.QFrame(Form)
            self.frames[f"{self.att.users[n]}"].setGeometry(QtCore.QRect(81 + (x - 1) * 61, 10 + (y - 1) * 61, 56 , 46))
            self.frames[f"{self.att.users[n]}"].setFrameShape(QtWidgets.QFrame.Box) 
            self.frames[f"{self.att.users[n]}"].setFrameShadow(QtWidgets.QFrame.Plain)
            self.frames[f"{self.att.users[n]}"].setLineWidth(2)
            self.frames[f"{self.att.users[n]}"].setObjectName("frame")
            # self.labels[f"{self.att.users[n]}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800") #green
            # self.labels[f"{self.att.users[n]}"].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c") #gray
            # self.labels[f"{self.att.users[n]}"].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d") #yellow
            self.labels[f"{self.att.users[n]}"] = QtWidgets.QLabel(self.frames[f"{self.att.users[n]}"])
            self.labels[f"{self.att.users[n]}"].setGeometry(QtCore.QRect(2, 2, 52, 42))
            if self.att.data[f"{self.att.users[n]}"]["check_time"] == None:
                self.labels[f"{self.att.users[n]}"].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")
            elif self.att.data[self.att.users[n]]["second_day"] != ['None'] and len(str(self.att.data[self.att.users[n]]["check_time"])) <= 10:
                self.labels[f"{self.att.users[n]}"].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
            elif self.att.data[self.att.users[n]]["second_day"] == ['None'] and len(str(self.att.data[self.att.users[n]]["check_time"])) <= 10:
                self.labels[f"{self.att.users[n]}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
            elif self.att.data[self.att.users[n]]["second_day"] != ['None'] and len(str(self.att.data[self.att.users[n]]["check_time"])) > 10:
                self.labels[f"{self.att.users[n]}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")

            self.labels[f"{self.att.users[n]}"].setAlignment(QtCore.Qt.AlignCenter)
            self.labels[f"{self.att.users[n]}"].setObjectName("label")
            self.labels[f"{self.att.users[n]}"].setText(_translate("Form", f"{self.att.users[n]}"))
            self.labels[f"{self.att.users[n]}"].setFont(font)
            self.labels[f"{self.att.users[n]}"].setAlignment(QtCore.Qt.AlignCenter)
            self.frames[f"{self.att.users[n]}"].show()

            n = n + 1
            
            
            if n != len(self.att.users)-2:
                if self.att.users[n] != self.att.users[n+1]:
                    x = 1
                    y = y + 1
                else:
                    x = x + 1

            elif n == len(self.att.users)-1:
                x = x + 1
            
            elif n == len(self.att.users):
                break
            
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
