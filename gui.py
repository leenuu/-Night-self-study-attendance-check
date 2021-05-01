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
        self.setup_pos()
        self.mapping()

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
                    self.labels[f"{self.att.data[user]['pos']}"].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
                elif self.att.data[user]["second_day"] == ['None']:
                    self.labels[f"{self.att.data[user]['pos']}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")

                print("출석완료.")
                print('\n',end='')

            elif self.att.check_time(self.att.data[user]["check_time"]):
                self.att.data[user]["check_time"] = self.att.data[user]["check_time"] + str(datetime.today().strftime("%H:%M:%S"))
                self.att.schedule_check(user)
                self.labels[f"{self.att.data[user]['pos']}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
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


    def setup_pos(self):
        x = 16
        xi = 1
        y = 925
        _translate = QtCore.QCoreApplication.translate
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(12)
        font.setBold(True)
        print(len(self.att.users))
        n = 1
        st = 0
        while True:
            if n <= 112:
                if st == 1:
                    y = y - 61
                    xi = xi * -1
                    st = 0

                elif n % 8 == 0:
                    st = 1
                    x = x + xi * 65
                else:
                    x = x + xi * 65
            elif n > 112 and n <= 124:
                if st == 1:
                    y = y - 61
                    xi = xi * -1
                    st = 0

                elif (n-112) % 6 == 0:
                    st = 1
                    x = x + xi * 65
                else:
                    x = x + xi * 65
            
            else:
                if n == 125:
                    x = 666
                    y = 925
                    xi = 1
                    st = 0

                if st == 1:
                    y = y - 61
                    xi = xi * -1
                    st = 0

                elif (n-124) % 9 == 0:
                    st = 1
                    x = x + xi * 65
                else:
                    x = x + xi * 65
           

            self.frames[f"{n}"] = QtWidgets.QFrame(Form)
            self.frames[f"{n}"].setGeometry(QtCore.QRect(x, y, 61 , 46))
            self.frames[f"{n}"].setFrameShape(QtWidgets.QFrame.Box) 
            self.frames[f"{n}"].setFrameShadow(QtWidgets.QFrame.Plain)
            self.frames[f"{n}"].setLineWidth(2)
            self.frames[f"{n}"].setObjectName("frame")
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800") #green
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c") #gray
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d") #yellow
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#323232") #black-gray
            self.labels[f"{n}"] = QtWidgets.QLabel(self.frames[f"{n}"])
            self.labels[f"{n}"].setGeometry(QtCore.QRect(2, 2, 57, 42))
            self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#323232") 
            # if self.att.data[f"{n}"]["check_time"] == None:
            #     self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")
            # elif self.att.data[n]["second_day"] != ['None'] and len(str(self.att.data[n]["check_time"])) <= 10:
            #     self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
            # elif self.att.data[n]["second_day"] == ['None'] and len(str(self.att.data[n]["check_time"])) <= 10:
            #     self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
            # elif self.att.data[n]["second_day"] != ['None'] and len(str(self.att.data[n]["check_time"])) > 10:
            #     self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")

            self.labels[f"{n}"].setAlignment(QtCore.Qt.AlignCenter)
            self.labels[f"{n}"].setObjectName("label")
            self.labels[f"{n}"].setText(_translate("Form", ""))
            self.labels[f"{n}"].setFont(font)
            self.labels[f"{n}"].setAlignment(QtCore.Qt.AlignCenter)
            self.frames[f"{n}"].show()
            
            print(f"n : {n} {x},{y},{61},{46}")

            if n == 268:
                break

            n = n + 1

    def mapping(self):
        # f"{self.att.data[self.att.users[n]]['pos']}"
        _translate = QtCore.QCoreApplication.translate
        for us in self.att.users:
            self.labels[f"{self.att.data[us]['pos']}"].setText(_translate("Form", f"{us}"))
            
            if self.att.data[us]["check_time"] == None:
                self.labels[f"{self.att.data[us]['pos']}"].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")
            elif self.att.data[us]["second_day"] != ['None'] and len(str(self.att.data[us]["check_time"])) <= 10:
                self.labels[f"{self.att.data[us]['pos']}"].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
            elif self.att.data[us]["second_day"] == ['None'] and len(str(self.att.data[us]["check_time"])) <= 10:
                self.labels[f"{self.att.data[us]['pos']}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
            elif self.att.data[us]["second_day"] != ['None'] and len(str(self.att.data[us]["check_time"])) > 10:
                self.labels[f"{self.att.data[us]['pos']}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")

            



            
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
