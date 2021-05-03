from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from main_for_t import attendance
# from barcode_reader import cam
import time
import  keyboard
import pyzbar.pyzbar as pyzbar 
import numpy as np 
import cv2

class Ui_Form(object):
    def __init__(self):
        self.att = attendance()
        self.attend_user_names = list()
        self.frames = dict()
        self.brts = dict()
        self.change_user = list()
        self.set_name_data()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1720, 980)
        self.label_txt = QtWidgets.QLabel(Form)
        self.label_txt.setGeometry(QtCore.QRect(1360, 30, 291, 161))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.label_txt.setFont(font)
        self.label_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_txt.setObjectName("label_txt")
    
        self.save_brt = QtWidgets.QPushButton(Form)
        self.save_brt.setGeometry(QtCore.QRect(1360, 220, 291, 41))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.save_brt.setFont(font)
        self.save_brt.setObjectName("save_brt")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.save_brt.clicked.connect(self.save_data)
        self.setup_pos()
        self.mapping()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_txt.setText(_translate("Form", ""))
        self.save_brt.setText(_translate("Form", "저장"))
    
    def set_name_data(self):
        for us in self.att.users:
            if self.att.day[datetime.today().weekday()] in self.att.data[us]["first_day"]:
                print(us)
                self.attend_user_names.append(us)

    def save_data(self):
        _translate = QtCore.QCoreApplication.translate
        print(self.change_user)
        for us in self.change_user:
            self.attend_brt(us)

        self.att.save()
        self.re_mapping()
        self.label_txt.setText(_translate("Form", "저장완료"))

    def change_brt_color(self, state, user):
        if self.brts[f"{self.att.data[user]['pos']}"][1] <= 1 and self.att.data[user]['second_day'] != ['None']:
            self.brts[f"{self.att.data[user]['pos']}"][1] = self.brts[f"{self.att.data[user]['pos']}"][1] + 1
        elif self.brts[f"{self.att.data[user]['pos']}"][1] == 0 and self.att.data[user]['second_day'] == ['None']:
            self.brts[f"{self.att.data[user]['pos']}"][1] = 2
        elif self.brts[f"{self.att.data[user]['pos']}"][1] == 2:
            self.brts[f"{self.att.data[user]['pos']}"][1] = 0

        if self.brts[f"{self.att.data[user]['pos']}"][1] == 0: 
            self.brts[f"{self.att.data[user]['pos']}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")        
        elif self.brts[f"{self.att.data[user]['pos']}"][1] == 1: 
            self.brts[f"{self.att.data[user]['pos']}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")        
        elif self.brts[f"{self.att.data[user]['pos']}"][1] == 2: 
            self.brts[f"{self.att.data[user]['pos']}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")    

        self.brts[f"{self.att.data[user]['pos']}"][2] = str(datetime.today().strftime("%Y-%m-%d"))
        if user not in self.change_user and self.brts[f"{self.att.data[user]['pos']}"][0] != 0:
            self.change_user.append(user)
        
        if self.brts[f"{self.att.data[user]['pos']}"][1] == 0:
            self.change_user.remove(user)


    def attend_brt(self, user):
        print(user)
        
        if self.brts[f"{self.att.data[user]['pos']}"][1] == 1:
            self.att.data[user]["last_date"] = str(datetime.today().strftime("%Y-%m-%d"))
            self.att.data[user]["check_time"] = str(datetime.today().strftime("%H:%M:%S")) 
            self.att.data[user]["count"] = self.att.data[user]["count"] + 1
            # self.att.schedule_check(user)

            print("출석완료.")
            print('\n',end='')

        elif self.brts[f"{self.att.data[user]['pos']}"][1] == 2 :
            if self.att.data[user]["check_time"] == None:
                self.att.data[user]["last_date"] = str(datetime.today().strftime("%Y-%m-%d"))
                self.att.data[user]["check_time"] = str(datetime.today().strftime("%H:%M:%S"))
                self.att.data[user]["count"] = self.att.data[user]["count"] + 1
            elif self.att.data[user]["check_time"] != None:
                self.att.data[user]["check_time"] = self.att.data[user]["check_time"] + '/' + str(datetime.today().strftime("%H:%M:%S"))
            # self.att.schedule_check(user)
            print("출석완료.")
            print('\n',end='')
        self.att.schedule_check(user)
                
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
            # self.frames[f"{n}"].setFrameShadow(QtWidgets.QFrame.Plain)
            self.frames[f"{n}"].setLineWidth(2)
            self.frames[f"{n}"].setObjectName("frame")
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800") #green
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c") #gray
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d") #yellow
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#323232") #black-gray
            self.brts[f"{n}"] = list()
            self.brts[f"{n}"].append(QtWidgets.QPushButton(self.frames[f"{n}"]))
            self.brts[f"{n}"][0].setGeometry(QtCore.QRect(2, 2, 57, 42))
            self.brts[f"{n}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#323232") 
            # self.brts[f"{n}"].setFlat(True)
            # self.brts[f"{n}"].setAlignment(QtCore.Qt.AlignCenter)
            self.brts[f"{n}"][0].setObjectName(f"{n}")
            self.brts[f"{n}"][0].setText(_translate("Form", ""))
            self.brts[f"{n}"][0].setFont(font)
            # self.brts[f"{n}"].setAlignment(QtCore.Qt.AlignCenter)
            self.brts[f"{n}"][0].setDisabled(True)
            self.brts[f"{n}"].append(0)
            self.brts[f"{n}"].append('')
            self.frames[f"{n}"].show()
            
            
            print(f"n : {n}  {x},{y},{61},{46}")

            if n == 268:
                break

            n = n + 1

    def mapping(self):
        # f"{self.att.data[self.att.users[n]]['pos']}"
        _translate = QtCore.QCoreApplication.translate
        for us in self.attend_user_names:
            self.brts[f"{self.att.data[us]['pos']}"][0].setText(_translate("Form", f"{us}\n{self.att.data[us]['pos']}"))
            self.brts[f"{self.att.data[us]['pos']}"][0].setDisabled(False)
            self.brts[f"{self.att.data[us]['pos']}"][0].clicked.connect(lambda state, user=us: self.change_brt_color(state, user))
            
            self.brts[f"{self.att.data[us]['pos']}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")
            
            if self.att.data[us]["second_day"] != ['None'] and self.att.data[us]["check_time"] != None and len(str(self.att.data[us]["check_time"])) <= 10:
                self.brts[f"{self.att.data[us]['pos']}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
                self.brts[f"{self.att.data[us]['pos']}"][1] = 1
            elif self.att.data[us]["second_day"] == ['None'] and self.att.data[us]["last_date"] == str(datetime.today().strftime("%Y-%m-%d")):
                self.brts[f"{self.att.data[us]['pos']}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
                self.brts[f"{self.att.data[us]['pos']}"][1] = 2
                self.brts[f"{self.att.data[us]['pos']}"][0].setDisabled(True)
            elif self.att.data[us]["second_day"] != ['None'] and len(str(self.att.data[us]["check_time"])) > 10:
                self.brts[f"{self.att.data[us]['pos']}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
                self.brts[f"{self.att.data[us]['pos']}"][1] = 2
                self.brts[f"{self.att.data[us]['pos']}"][0].setDisabled(True)

    def re_mapping(self):
        for us in self.change_user:
            self.brts[f"{self.att.data[us]['pos']}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
            self.brts[f"{self.att.data[us]['pos']}"][1] = 2
            self.brts[f"{self.att.data[us]['pos']}"][0].setDisabled(True)
        
        self.change_user = []

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())