from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from main_for_t_ver2 import attendance
import time

class Ui_Form(object):
    def __init__(self):
        self.att = attendance()
        # self.attend_user_names = self.get_att_users()
        self.log = self.att.log
        self.frames = dict()
        self.brts = dict()
        self.attend_users = self.set_attend_users()
        self.change_user = list()
        self.class_time = 1


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

        self.attend_absent = QtWidgets.QRadioButton(Form)
        self.attend_absent.setGeometry(QtCore.QRect(1360, 400, 291, 30))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.attend_absent.setFont(font)
        self.attend_absent.setObjectName("attend_absent")

        self.late_ealy = QtWidgets.QRadioButton(Form)
        self.late_ealy.setGeometry(QtCore.QRect(1360, 450, 291, 30))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.late_ealy.setFont(font)
        self.late_ealy.setObjectName("late_ealy")

        self.first_class = QtWidgets.QPushButton(Form)
        self.first_class.setGeometry(QtCore.QRect(1360, 280, 291, 41))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.first_class.setFont(font)
        self.first_class.setCheckable(False)
        self.first_class.setAutoRepeat(False)
        self.first_class.setAutoExclusive(False)
        self.first_class.setAutoDefault(False)
        self.first_class.setFlat(False)
        self.first_class.setObjectName("first_class")

        self.second_class = QtWidgets.QPushButton(Form)
        self.second_class.setGeometry(QtCore.QRect(1360, 340, 291, 41))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.second_class.setFont(font)
        self.second_class.setCheckable(False)
        self.second_class.setAutoRepeat(False)
        self.second_class.setAutoExclusive(False)
        self.second_class.setAutoDefault(False)
        self.second_class.setFlat(False)
        self.second_class.setObjectName("second_class")

        self.memo = QtWidgets.QPlainTextEdit(Form)
        self.memo.setGeometry(QtCore.QRect(1360, 500, 291, 350))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.memo.setFont(font)
        self.memo.setObjectName("memo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.first_class.setDisabled(True)
        self.attend_absent.setChecked(True)
        # self.save_brt.clicked.connect(self.save_data)
        self.attend_absent.clicked.connect(self.class_time_radio)
        self.late_ealy.clicked.connect(self.class_time_radio)
        self.setup_pos()
        self.mapping()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_txt.setText(_translate("Form", ""))
        self.save_brt.setText(_translate("Form", "저장"))
        self.attend_absent.setText(_translate("Form", "    출석   /   결석"))
        self.late_ealy.setText(_translate("Form", "    지각   /   조퇴"))
        self.first_class.setText(_translate("Form", "1 교시"))
        self.second_class.setText(_translate("Form", "2 교시"))
        self.memo.setPlainText(_translate("Form", self.log))
    
    def class_time_radio(self):
        if self.attend_absent.isChecked():
            print(1)
            self.class_time = 1
        elif self.late_ealy.isChecked():
            print(2)
            self.class_time = 2

    def set_attend_users(self):
        users = list()
        for user in self.att.user_names:
            if self.att.day[datetime.today().weekday()] in self.att.data[user]["first_day"]:
                users.append(user)
        return users

    def change_brt_color(self, state, user):
        if self.class_time == 1:
            brt = self.brts[f"{self.att.data[user]['pos']}"]
            if brt[1] == 0:
                brt[1] = 1
                print(brt[1])
                brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
            elif brt[1] == 1:
                brt[1] = 2
                print(brt[1])
                brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#fc0000")
            elif brt[1] == 2:
                brt[1] = 0
                print(brt[1])
                brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")
            
                
        elif self.class_time == 2:
            brt = self.brts[f"{self.att.data[user]['pos']}"]
            if brt[1] == 0:
                brt[1] = 3
                print(brt[1])
                brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
            elif brt[1] == 3:
                brt[1] = 4
                print(brt[1])
                brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#fa661d")
            elif brt[1] == 4:
                brt[1] = 0
                print(brt[1])
                brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")
        if brt[0] != 0 and user not in self.change_user:
            self.change_user.append(user)

    def mapping(self):
        _translate = QtCore.QCoreApplication.translate
        if self.class_time == 1:
            for us in self.attend_users:
                brt = self.brts[f"{self.att.data[us]['pos']}"]
                brt[0].setText(_translate("Form", f"{us}\n{self.att.data[us]['pos']}"))
                brt[0].setDisabled(False)
                brt[0].clicked.connect(lambda state, user=us: self.change_brt_color(state, user))
                if self.att.data[us]['first_check_time'] == None:
                    brt[1] = 0
                elif self.att.data[us]['first_check_time'] == "결석":
                    brt[1] = 2
                elif "지각" in self.att.data[us]['first_check_time']:
                    brt[1] = 4
                elif self.att.data[us]['first_check_time'] == "조퇴":
                    brt[1] = 4
                else:
                    brt[1] = 1

                if brt[1] == 0:
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")
                elif brt[1] == 1:
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
                    brt[0].setDisabled(True)
                elif brt[1] == 2:
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "FC0000")
                    brt[0].setDisabled(True)
                elif brt[1] == 3:
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
                    brt[0].setDisabled(True)
                elif brt[1] == 4:
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#FA661D")
                    brt[0].setDisabled(True)
    
        elif self.class_time == 2:
            for us in self.attend_users:
                if self.att.day[datetime.today().weekday()] in self.att.data[us]['second_day']:
                    brt = self.brts[f"{self.att.data[us]['pos']}"]
                    brt[0].setText(_translate("Form", f"{us}\n{self.att.data[us]['pos']}"))
                    brt[0].setDisabled(False)
                    brt[0].clicked.connect(lambda state, user=us: self.change_brt_color(state, user))
                    if self.att.data[us]['second_check_time'] == None:
                        brt[1] = 0
                    elif self.att.data[us]['second_check_time'] == "결석":
                        brt[1] = 2
                    elif "지각" in self.att.data[us]['second_check_time']:
                        brt[1] = 4
                    elif self.att.data[us]['second_check_time'] == "조퇴":
                        brt[1] = 4
                    else:
                        brt[1] = 1

                    if brt[1] == 0:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")
                    elif brt[1] == 1:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
                        brt[0].setDisabled(True)
                    elif brt[1] == 2:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "FC0000")
                        brt[0].setDisabled(True)
                    elif brt[1] == 3:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
                        brt[0].setDisabled(True)
                    elif brt[1] == 4:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#FA661D")
                        brt[0].setDisabled(True)
                
    def re_mapping(self):
        _translate = QtCore.QCoreApplication.translate
        if self.class_time == 1:
            for us in self.change_user:
                brt = self.brts[f"{self.att.data[us]['pos']}"]
                brt[0].setText(_translate("Form", f"{us}\n{self.att.data[us]['pos']}"))
                brt[0].setDisabled(False)
                brt[0].clicked.connect(lambda state, user=us: self.change_brt_color(state, user))
                if self.att.data[us]['first_check_time'] == None:
                    brt[1] = 0
                elif self.att.data[us]['first_check_time'] == "결석":
                    brt[1] = 2
                elif "지각" in self.att.data[us]['first_check_time']:
                    brt[1] = 4
                elif self.att.data[us]['first_check_time'] == "조퇴":
                    brt[1] = 4
                else:
                    brt[1] = 1

                if brt[1] == 0:
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")
                elif brt[1] == 1:
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
                    brt[0].setDisabled(True)
                elif brt[1] == 2:
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "FC0000")
                    brt[0].setDisabled(True)
                elif brt[1] == 3:
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
                    brt[0].setDisabled(True)
                elif brt[1] == 4:
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#FA661D")
                    brt[0].setDisabled(True)
    
        elif self.class_time == 2:
            for us in self.change_user:
                if self.att.day[datetime.today().weekday()] in self.att.data[us]['second_day']:
                    brt = self.brts[f"{self.att.data[us]['pos']}"]
                    brt[0].setText(_translate("Form", f"{us}\n{self.att.data[us]['pos']}"))
                    brt[0].setDisabled(False)
                    brt[0].clicked.connect(lambda state, user=us: self.change_brt_color(state, user))
                    if self.att.data[us]['second_check_time'] == None:
                        brt[1] = 0
                    elif self.att.data[us]['second_check_time'] == "결석":
                        brt[1] = 2
                    elif "지각" in self.att.data[us]['second_check_time']:
                        brt[1] = 4
                    elif self.att.data[us]['second_check_time'] == "조퇴":
                        brt[1] = 4
                    else:
                        brt[1] = 1

                    if brt[1] == 0:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")
                    elif brt[1] == 1:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
                        brt[0].setDisabled(True)
                    elif brt[1] == 2:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "FC0000")
                        brt[0].setDisabled(True)
                    elif brt[1] == 3:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
                        brt[0].setDisabled(True)
                    elif brt[1] == 4:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#FA661D")
                        brt[0].setDisabled(True)

        self.change_user = []

    def setup_pos(self):
        x = 16
        xi = 1
        y = 925
        _translate = QtCore.QCoreApplication.translate
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(12)
        font.setBold(True)
        # print(len(self.att.users))
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
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#02f800") #green 출석 1
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c") #gray 선택 X 0
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d") #yellow 지각 3
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#323232") #black-gray 자리 X
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#FA661D") #orange 조퇴 4
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#453CF3") #blue 
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#FC0000") # red 결석 2
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
