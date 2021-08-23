from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from main import attendance
# from barcode_reader import cam
import time
import  keyboard
import pyzbar.pyzbar as pyzbar 
import numpy as np 
import cv2

class camThread(QtCore.QThread):
    user = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__()
        
        self.main = parent
        self.isRun = False
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


    def run(self):
        while self.isRun:
            ret, frame = self.capture.read()
            cv2.imshow("VideoFrame", frame)
            if cv2.waitKey(1) == 27:
                pass
            if keyboard.is_pressed('esc'):
                self.capture.release()
                self.isRun = False
                self.user.emit("0")
                return
            elif keyboard.is_pressed('enter'):
                try:
                    cv2.imwrite('barcode.png',frame, params=[cv2.IMWRITE_JPEG_QUALITY,0])
                    im = cv2.imread('barcode.png') 
                    decodedObjects = self.decode(im)
                    data = str(int(decodedObjects[0].data))
                    self.user.emit(data)
                except IndexError:
                    self.user.emit("1")

    def decode(self,im):
        decodedObjects = pyzbar.decode(im) 
        return decodedObjects


class Ui_Form(object):
    def __init__(self):
        self.att = attendance()
        self.cam_data = camThread(self)
        self.cam_data.user.connect(self.use_cam)
        self.attend_user_names = list()
        self.frames = dict()
        self.labels = dict()
        self.set_name_data()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1720, 980)
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(16)
        Form.setFont(font)
        self.attend_brt = QtWidgets.QPushButton(Form)
        self.attend_brt.setGeometry(QtCore.QRect(1560, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.attend_brt.setFont(font)
        self.attend_brt.setObjectName("attend_brt")
        self.input_user = QtWidgets.QLineEdit(Form)
        self.input_user.setGeometry(QtCore.QRect(1360, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.input_user.setFont(font)
        self.input_user.setObjectName("input_user")
        self.label_txt = QtWidgets.QLabel(Form)
        self.label_txt.setGeometry(QtCore.QRect(1360, 160, 291, 161))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.label_txt.setFont(font)
        self.label_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_txt.setObjectName("label_txt")
        self.switching_cam_brt = QtWidgets.QPushButton(Form)
        self.switching_cam_brt.setGeometry(QtCore.QRect(1360, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.switching_cam_brt.setFont(font)
        self.switching_cam_brt.setObjectName("switching_cam_brt")
        self.switching_num_brt = QtWidgets.QPushButton(Form)
        self.switching_num_brt.setGeometry(QtCore.QRect(1460, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.switching_num_brt.setFont(font)
        self.switching_num_brt.setObjectName("switching_num_brt")
        self.switching_num_brt.setDisabled(True)

        self.save_brt = QtWidgets.QPushButton(Form)
        self.save_brt.setGeometry(QtCore.QRect(1560, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.save_brt.setFont(font)
        self.save_brt.setObjectName("save_brt")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.attend_brt.clicked.connect(self.attend)
        self.save_brt.clicked.connect(self.save_data)
        self.switching_cam_brt.clicked.connect(self.switching_cam)
        self.switching_num_brt.clicked.connect(self.switching_num)
        self.setup_pos()
        self.mapping()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.attend_brt.setText(_translate("Form", "출석"))
        self.label_txt.setText(_translate("Form", ""))
        self.switching_cam_brt.setText(_translate("Form", "학생증"))
        self.switching_num_brt.setText(_translate("Form", "학번"))
        self.save_brt.setText(_translate("Form", "저장"))
    
    def set_name_data(self):
        for us in self.att.users:
            if self.att.day[datetime.today().weekday()] in self.att.data[us]["first_day"]:
                print(us)
                self.attend_user_names.append(us)


    def switching_cam(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_txt.setText(_translate("Form", "학생증"))
        self.switching_cam_brt.setDisabled(True)
        self.switching_num_brt.setDisabled(False)
        self.attend_brt.setDisabled(True)
        self.cam_data.isRun = True
        self.cam_data.start()
        
    def use_cam(self, user):
        if self.cam_data.isRun == False:
            self.switching_cam_brt.setDisabled(False)
            self.switching_num_brt.setDisabled(True)
            self.attend_brt.setDisabled(False)
        print(user)
    
    def switching_num(self):
        pass
        # _translate = QtCore.QCoreApplication.translate
        # self.label_txt.setText(_translate("Form", "학번"))
        # self.switching_cam_brt.setDisabled(False)
        # self.switching_num_brt.setDisabled(True)

    def save_data(self):
        _translate = QtCore.QCoreApplication.translate
        self.att.save()
        self.label_txt.setText(_translate("Form", "저장완료"))

    def attend(self):
        _translate = QtCore.QCoreApplication.translate
        user = str(self.input_user.text())
        print(user)
        try:
            if user in self.attend_user_names:
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
            else:
                self.label_txt.setText(_translate("Form","오늘 야자 학생이 \n아닙니다."))
                print("오늘 야자 학생이 아닙니다.")
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
        for us in self.attend_user_names:
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
