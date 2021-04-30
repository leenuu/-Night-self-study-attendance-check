from datetime import datetime
import openpyxl

class attendance:
    def __init__(self):
        self.day = ['월', '화', '수', '목', '금', '토', '일']
        self.col_date = 0
        self.data = self.load()
        self.users = self.user_names()
        try:
            self.schedule_check_init()
        
        except FileNotFoundError:
            self.schedule_init()
            self.schedule_check_init()

    def user_names(self):
        users = list()
        num = 1
        files = openpyxl.load_workbook('data.xlsx')
        xlsx = files.active
        while True:
            if xlsx.cell(row=num, column=1).value != None:
                users.append(xlsx.cell(row=num, column=1).value)
                num = num + 1
            else:
                break
        return users

    def load(self):
        data = dict()
        num = 1
        files = openpyxl.load_workbook('data.xlsx')
        xlsx = files.active

        sc_files = openpyxl.load_workbook('data.xlsx')

        while True:
            if xlsx.cell(row=num, column=1).value != None:
                data[xlsx.cell(row=num, column=1).value] = {"last_date" : str(xlsx.cell(row=num, column=2).value).split(' ')[0], "count" : int(xlsx.cell(row=num, column=4).value), "day" : str(xlsx.cell(row=num, column=3).value).split(','), "check_time": }
            elif xlsx.cell(row=num, column=1).value == None:
                break
            num = num + 1
        # print(str(xlsx.cell(row=1, column=2).value).split(' '))
        # print(data["031423-이건우"]["last_date"])
        return data

    def save(self):
        files = openpyxl.load_workbook('data.xlsx')
        ds = files.active

        num = 1
        while True:
            if ds.cell(row=num, column=1).value != None:
                ds.cell(row=num, column=2).value = self.data[ds.cell(row=num, column=1).value]["last_date"]
                ds.cell(row=num, column=4).value = self.data[ds.cell(row=num, column=1).value]["count"]    
                
            elif ds.cell(row=num, column=1).value == None:
                break
            num = num + 1
        
        files.save("data.xlsx")
    
    def schedule_init(self):
        files = openpyxl.load_workbook('data.xlsx')
        ds = files.active

        wb = openpyxl.Workbook()
        ws = wb.active

        num = 2
        ws.cell(row=1, column=1).value = "학번-이름"
        ws.cell(row=1, column=2).value = "출석 수"

        while True:
            if ds.cell(row=num-1, column=1).value != None:
                ws.cell(row=num, column=1).value = ds.cell(row=num-1, column=1).value
                ws.cell(row=num, column=2).value = self.data[ds.cell(row=num-1, column=1).value]["count"]    
                
            elif ds.cell(row=num-1, column=1).value == None:
                break
            num = num + 1
        
        wb.save("schedule.xlsx")


    def schedule_check_init(self):
        files = openpyxl.load_workbook('schedule.xlsx', read_only=False, data_only=True)
        ds = files.active

        self.col_date = 3
        while True:
            if ds.cell(row=1, column=self.col_date).value == None and ds.cell(row=1, column=self.col_date).value != str(datetime.today().strftime("%Y-%m-%d")):
                ds.cell(row=1, column=self.col_date).value = str(datetime.today().strftime("%Y-%m-%d")) + f" {self.day[datetime.today().weekday()]}"
                break
            elif ds.cell(row=1, column=self.col_date).value == str(datetime.today().strftime("%Y-%m-%d")) + f" {self.day[datetime.today().weekday()]}":
                break

            else:
                pass
            
            self.col_date = self.col_date + 1
                
        files.save("schedule.xlsx")

    def schedule_check(self, user):
        files = openpyxl.load_workbook('schedule.xlsx', read_only=False, data_only=True)
        ds = files.active

        user_num = 2
        while True:
            if ds.cell(row=user_num, column=1).value == user:
                ds.cell(row=user_num, column=self.col_date).value = str(datetime.today().strftime("%H:%M:%S")) + "/"
                ds.cell(row=user_num, column=2).value = self.data[ds.cell(row=user_num-1, column=1).value]["count"]    
                break
            user_num = user_num + 1
        files.save("schedule.xlsx")
    

    # print(data["031402-강준"]["count"])
    def run(self):
        while True:
            print("야자 출석 명단")
            for i in self.users:
                if self.day[datetime.today().weekday()] in self.data[i]["day"] and self.data[i]["last_date"] != str(datetime.today().strftime("%Y-%m-%d")):
                    print(f'{i} : X')
                elif self.day[datetime.today().weekday()] in self.data[i]["day"] and self.data[i]["last_date"] == str(datetime.today().strftime("%Y-%m-%d")):
                    print(f'{i} : O')
            print('\n',end='')

            print("학번-이름 : ",end='')
            user = input()

            if user == "stop":
                break
            
            if user == "save":
                self.save()
                break

            try:
                if str(datetime.today().strftime("%Y-%m-%d")) == self.data[user]["last_date"] and (self.data[user]["check_time"] - datetime.now()).second / 3600 < 1:
                    print("이미 춣석 하셨습니다.")
                    print('\n',end='')
                
                elif str(datetime.today().strftime("%Y-%m-%d")) != self.data[user]["last_date"] and self.data[user]["check_time"] == None:
                    self.data[user]["last_date"] = str(datetime.today().strftime("%Y-%m-%d"))
                    self.data[user]["check_time"] = datetime.now()
                    self.data[user]["count"] = self.data[user]["count"] + 1
                    self.schedule_check(user)
                    print("출석완료.")
                    print('\n',end='')
                
                elif str(datetime.today().strftime("%Y-%m-%d")) != self.data[user]["last_date"] and (self.data[user]["check_time"] - datetime.now()).second / 3600 >= 1:
                    self.schedule_check(user)
                    print("출석완료.")
                    print('\n',end='')

            except KeyError:
                pass
    

at = attendance()
at.run()
# at.schedule_init()
# at.schedule_edit()

