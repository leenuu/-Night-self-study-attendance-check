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
        self.delete_users = self.att.delete_check()
        self.att.attend_user_names = self.attend_users
        self.change_users = list()
        self.init_connect = 1
        self.init_save = 1
        self.init_save_2 = 1
        self.class_time = 1
        self.color_changes = 1

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

        self.delete_brt = QtWidgets.QPushButton(Form)
        self.delete_brt.setGeometry(QtCore.QRect(1510, 220, 141, 41))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.delete_brt.setFont(font)
        self.delete_brt.setObjectName("delete_brt")

        self.save_brt = QtWidgets.QPushButton(Form)
        self.save_brt.setGeometry(QtCore.QRect(1360, 220, 141, 41))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.save_brt.setFont(font)
        self.save_brt.setObjectName("save_brt")

        self.attend = QtWidgets.QRadioButton(Form)
        self.attend.setGeometry(QtCore.QRect(1360, 400, 291, 30))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.attend.setFont(font)
        self.attend.setObjectName("attend")
        self.absent = QtWidgets.QRadioButton(Form)
        self.absent.setGeometry(QtCore.QRect(1360, 450, 291, 30))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.absent.setFont(font)
        self.absent.setObjectName("absent")

        self.late = QtWidgets.QRadioButton(Form)
        self.late.setGeometry(QtCore.QRect(1360, 500, 291, 30))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.late.setFont(font)
        self.late.setObjectName("late")
        self.ealy = QtWidgets.QRadioButton(Form)
        self.ealy.setGeometry(QtCore.QRect(1360, 550, 291, 30))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.ealy.setFont(font)
        self.ealy.setObjectName("ealy")

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
        self.memo.setGeometry(QtCore.QRect(1360, 600, 291, 311))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.memo.setFont(font)
        self.memo.setObjectName("memo")

        self.green = QtWidgets.QFrame(Form)
        self.green.setGeometry(QtCore.QRect(1570, 400, 81, 31))
        self.green.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.green.setFrameShadow(QtWidgets.QFrame.Raised)
        self.green.setObjectName("green")
        self.green.setStyleSheet("QWidget { background-color: %s }" %  "#02f800")

        self.red = QtWidgets.QFrame(Form)
        self.red.setGeometry(QtCore.QRect(1570, 450, 81, 31))
        self.red.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.red.setFrameShadow(QtWidgets.QFrame.Raised)
        self.red.setObjectName("red")
        self.red.setStyleSheet("QWidget { background-color: %s }" %  "#fc0000")

        self.yellow = QtWidgets.QFrame(Form)
        self.yellow.setGeometry(QtCore.QRect(1570, 500, 81, 31))
        self.yellow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.yellow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.yellow.setObjectName("yellow")
        self.yellow.setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")

        self.orange = QtWidgets.QFrame(Form)
        self.orange.setGeometry(QtCore.QRect(1570, 550, 81, 31))
        self.orange.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.orange.setFrameShadow(QtWidgets.QFrame.Raised)
        self.orange.setObjectName("orange")
        self.orange.setStyleSheet("QWidget { background-color: %s }" %  "#9966ff")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        if type(self.delete_users) == int:
            self.delete_brt.setDisabled(True)    

        self.first_class.setDisabled(True)
        self.attend.setChecked(True)

        self.save_brt.clicked.connect(self.save)
        self.delete_brt.clicked.connect(self.delete_user)
        self.first_class.clicked.connect(self.switching_class_time)
        self.second_class.clicked.connect(self.switching_class_time)
        self.attend.clicked.connect(self.class_time_radio)
        self.absent.clicked.connect(self.class_time_radio)
        self.ealy.clicked.connect(self.class_time_radio)
        self.late.clicked.connect(self.class_time_radio)
        
        self.setup_pos()
        self.mapping()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_txt.setText(_translate("Form", ""))
        self.save_brt.setText(_translate("Form", "저장"))
        self.delete_brt.setText(_translate("Form", "삭제"))
        self.attend.setText(_translate("Form", "  출 석"))
        self.absent.setText(_translate("Form", "  결 석"))
        self.late.setText(_translate("Form", "  지 각"))
        self.ealy.setText(_translate("Form", "  조 퇴"))
        self.first_class.setText(_translate("Form", "1 교시"))
        self.second_class.setText(_translate("Form", "2 교시"))
        self.memo.setPlainText(_translate("Form", self.log))
        
    def delete_user(self):
        self.delete_brt.setDisabled(True)
        for us in self.delete_users:
            self.att.delete_user(us)

    def save(self):
        _translate = QtCore.QCoreApplication.translate
        self.log = self.memo.toPlainText()
        
        if self.init_save == 1 and self.class_time == 1:
            self.check_user(self.attend_users)
            self.att.save_schedule(self.attend_users)
            self.init_save = 0

        elif self.init_save_2 == 1 and self.class_time == 2:
            self.check_user(self.attend_users)
            self.att.save_schedule(self.attend_users)
            self.init_save_2 = 0

        else:
            self.check_user(self.change_users)
            self.att.save_schedule(self.change_users)
            pass
        self.att.log_save(self.log)
        self.re_mapping()
        print("saved")

    def switching_class_time(self):
        if self.class_time == 1:
            print("2 s")
            self.class_time = 2
            self.first_class.setDisabled(False)
            self.second_class.setDisabled(True)
            self.mapping()
            self.change_users = []

        elif self.class_time == 2:
            print("1 s")
            self.class_time = 1
            self.first_class.setDisabled(True)
            self.second_class.setDisabled(False)
            self.mapping()
            self.change_users = []

    def class_time_radio(self):
        if self.attend.isChecked():
            print(1)
            self.color_changes = 1
        elif self.absent.isChecked():
            print(2)
            self.color_changes = 2
        elif self.late.isChecked():
            print(3)
            self.color_changes = 3
        elif self.ealy.isChecked():
            print(4)
            self.color_changes = 4

    def set_attend_users(self):
        users = list()
        for user in self.att.user_names:
            if self.att.day[datetime.today().weekday()] in self.att.data[user]["first_day"] or self.att.day[datetime.today().weekday()] in self.att.data[user]["second_day"]:
                users.append(user)

        return users

    def change_brt_color(self, state, user):
        print("clicked")
        if self.color_changes == 1:
            self.brts[f"{self.att.data[user]['pos']}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
            self.brts[f"{self.att.data[user]['pos']}"][1] = 1
        elif self.color_changes == 2:
            self.brts[f"{self.att.data[user]['pos']}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#fc0000")
            self.brts[f"{self.att.data[user]['pos']}"][1] = 2
        elif self.color_changes == 3: 
            self.brts[f"{self.att.data[user]['pos']}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
            self.brts[f"{self.att.data[user]['pos']}"][1] = 3
        elif self.color_changes == 4:
            self.brts[f"{self.att.data[user]['pos']}"][0].setStyleSheet("QWidget { background-color: %s }" %  "#9966ff")
            self.brts[f"{self.att.data[user]['pos']}"][1] = 4
        if self.init_save == 0 and self.class_time == 1:
            if self.brts[f"{self.att.data[user]['pos']}"][0] != 1 and user not in self.change_users:
                self.change_users.append(user)
            elif self.brts[f"{self.att.data[user]['pos']}"][0] == 1 and user in self.change_users:
                self.change_users.remove(user)

        elif self.init_save_2 == 0 and self.class_time == 2:
            if self.brts[f"{self.att.data[user]['pos']}"][0] != 1 and user not in self.change_users:
                self.change_users.append(user)
            elif self.brts[f"{self.att.data[user]['pos']}"][0] == 1 and user in self.change_users:
                self.change_users.remove(user)

    def check_user(self, users):

        for us in users:
            brt = self.brts[f"{self.att.data[us]['pos']}"]
            # print(brt[1])
            if brt[1] == 1:
                self.att.attend_check(us, self.class_time)
            elif brt[1] == 2:
                self.att.absent_check(us, self.class_time)
            elif brt[1] == 3:
                self.att.late_check(us, self.class_time)
            elif brt[1] == 4:
                self.att.early_leave_check(us, self.class_time)

    def mapping(self):
        _translate = QtCore.QCoreApplication.translate
        if self.class_time == 1:
            for us in self.attend_users:
                
                brt = self.brts[f"{self.att.data[us]['pos']}"]
                if self.init_connect == 1:
                    print("1, init_connect")
                    brt[0].clicked.connect(lambda state, user=us: self.change_brt_color(state, user))

                if self.att.day[datetime.today().weekday()] in self.att.data[us]['first_day']:

                    brt[0].setText(_translate("Form", f"{us}\n{self.att.data[us]['pos']}"))
                    brt[0].setDisabled(False)
                    
                    if us in self.delete_users:
                        brt[1] = 5
                        
                    if brt[1] != 5:
                        if self.att.data[us]['first_check_time'] == None or self.att.data[us]['first_check_time'] == "출석":
                            brt[1] = 1
                        elif self.att.data[us]['first_check_time'] == "결석":
                            brt[1] = 2
                        elif self.att.data[us]['first_check_time'] == "지각":
                            brt[1] = 3
                        elif self.att.data[us]['first_check_time'] == "조퇴":
                            brt[1] = 4


                    if brt[1] == 1:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 2:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#fc0000")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 3:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 4:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9966ff")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 5:
                        brt[0].setDisabled(True)
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")

                    print(us, brt[1], self.att.data[us]['first_day'])

                else:
                    print(us)
                    brt = self.brts[f"{self.att.data[us]['pos']}"]
                    brt[0].setText(_translate("Form", ""))
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#323232") 
                    brt[0].setDisabled(True) 
                    brt[1] = 0               
    
        elif self.class_time == 2:
            for us in self.attend_users:
                # print(us, self.att.data[us]['second_day'])
                if self.att.day[datetime.today().weekday()] in self.att.data[us]['second_day']:
                    # if self.att.day[datetime.today().weekday()] in self.att.data[us]['second_day']:
                    brt = self.brts[f"{self.att.data[us]['pos']}"]
                    if self.init_connect == 1:
                        print("2, init_connect")
                        brt[0].clicked.connect(lambda state, user=us: self.change_brt_color(state, user))

                    brt[0].setText(_translate("Form", f"{us}\n{self.att.data[us]['pos']}"))
                    brt[0].setDisabled(False)

                    if us in self.delete_users:
                        brt[1] = 5

                    if brt[1] != 5:
                        if self.att.data[us]['second_check_time'] == None or self.att.data[us]['second_check_time'] == "출석":
                            brt[1] = 1
                        elif self.att.data[us]['second_check_time'] == "결석":
                            brt[1] = 2
                        elif self.att.data[us]['second_check_time'] == "지각":
                            brt[1] = 3
                        elif self.att.data[us]['second_check_time'] == "조퇴":
                            brt[1] = 4                            


                    if brt[1] == 1:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 2:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#fd0000")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 3:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 4:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9966ff")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 5:
                        brt[0].setDisabled(True)
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")

                    print(us, brt[1], self.att.data[us]['second_check_time'])


                else:
                    print(us)
                    brt = self.brts[f"{self.att.data[us]['pos']}"]
                    brt[0].setText(_translate("Form", ""))
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#323232") 
                    brt[0].setDisabled(True)
                    brt[1] = 0 

        if self.init_connect == 1:
            self.init_connect = 0

    def re_mapping(self):
        _translate = QtCore.QCoreApplication.translate
        if self.class_time == 1:
            for us in self.change_users:
                if self.att.day[datetime.today().weekday()] in self.att.data[us]['first_day']:
                    brt = self.brts[f"{self.att.data[us]['pos']}"]
                    brt[0].setText(_translate("Form", f"{us}\n{self.att.data[us]['pos']}"))
                    brt[0].setDisabled(False)

                    if us in self.delete_users:
                        brt[1] = 5

                    if brt[1] != 5:

                        if self.att.data[us]['first_check_time'] == None or self.att.data[us]['first_check_time'] == "출석" :
                            brt[1] = 1
                        elif self.att.data[us]['first_check_time'] == "결석":
                            brt[1] = 2
                        elif self.att.data[us]['first_check_time'] == "지각":
                            brt[1] = 3
                        elif self.att.data[us]['first_check_time'] == "조퇴":
                            brt[1] = 4
                        

                    if brt[1] == 1:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 2:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#fc0000")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 3:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 4:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9966ff")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 5:
                        brt[0].setDisabled(True)
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")
                    print(us, brt[1])

        elif self.class_time == 2:
            for us in self.change_users:
                if self.att.day[datetime.today().weekday()] in self.att.data[us]['second_day']:
                    brt = self.brts[f"{self.att.data[us]['pos']}"]
                    brt[0].setText(_translate("Form", f"{us}\n{self.att.data[us]['pos']}"))
                    brt[0].setDisabled(False)

                    if us in self.delete_users:
                        brt[1] = 5

                    if brt[1] != 5:

                        if self.att.data[us]['second_check_time'] == None or self.att.data[us]['second_check_time'] == "출석":
                            brt[1] = 1
                        elif self.att.data[us]['second_check_time'] == "결석":
                            brt[1] = 2
                        elif self.att.data[us]['second_check_time'] == "지각" :
                            brt[1] = 3
                        elif self.att.data[us]['second_check_time'] == "조퇴":
                            brt[1] = 4
                        

                    if brt[1] == 1:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#02f800")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 2:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#fc0000")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 3:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#ffff4d")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 4:
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9966ff")
                        # brt[0].setDisabled(True)
                    elif brt[1] == 5:
                        brt[0].setDisabled(True)
                        brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#9c9c9c")
                    print(us, brt[1])

                elif self.att.data[us]['second_day'] == []:
                    print(us)
                    brt = self.brts[f"{self.att.data[us]['pos']}"]
                    brt[0].setText(_translate("Form", ""))
                    brt[0].setStyleSheet("QWidget { background-color: %s }" %  "#323232") 
                    brt[0].setDisabled(True)
                
        self.change_users = []

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
            # self.labels[f"{n}"].setStyleSheet("QWidget { background-color: %s }" %  "#9966ff") #orange 조퇴 4
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
    app.exec_()
    print(1)
    ui.att.schedule_count()
    ui.att.save_data(ui.att.user_names)
