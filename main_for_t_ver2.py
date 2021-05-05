from datetime import datetime
import openpyxl
import os

class attendance:
    def __init__(self):
        self.day = ['월', '화', '수', '목', '금', '토', '일']
        self.path_serv_data = os.path.join(os.getcwd(), 'serv.xlsx')
        self.path_data = os.path.join(os.getcwd(), 'data.xlsx')
        self.path_schedule = os.path.join(os.getcwd(), 'schedule.xlsx') 
        self.col_num_data = 0
        self.serv_col_num_data = 0
        self.user_names = list()
        self.data = self.data_load()
        
        try:
            self.schedule_check_init()
            

        except FileNotFoundError:
            self.schedule_init()
            
            self.schedule_check_init()

        try:
            self.serv_data = self.serv_data_load()

        except FileNotFoundError:
            self.serv_data_init()
            self.serv_data = self.serv_data_load()


    def data_load(self):
        data = dict()
        row = 2
        data_files = openpyxl.load_workbook(self.path_data)
        data_xlsx = data_files.active

        while True:
            if data_xlsx.cell(row=row, column=1).value != None:
                user_id = row - 2
                user = str(data_xlsx.cell(row=row, column=1).value)
                last_date = str(data_xlsx.cell(row=row, column=2).value).split(' ')[0]
                first_day = str(data_xlsx.cell(row=row, column=3).value).split(',')
                second_day = (lambda day: None if day == None else str(day).split(','))(data_xlsx.cell(row=row, column=4).value)
                attend_count = int(data_xlsx.cell(row=row, column=5).value)
                early_leave_count = int(data_xlsx.cell(row=row, column=6).value)
                late_count = int(data_xlsx.cell(row=row, column=7).value)
                absent_count = int(data_xlsx.cell(row=row, column=8).value)
                pos = int(data_xlsx.cell(row=row, column=9).value)
                data[user] = {"id" : user_id, "last_date" : last_date, "first_day" : first_day, "second_day" : second_day, "attend_count" : attend_count, "early_leave_count" : early_leave_count, "late_count": late_count, "absent_count" : absent_count, "pos" : pos, "check_time": None }
                
                self.user_names.append(user)
                row = row + 1

            elif data_xlsx.cell(row=row, column=1).value == None:
                break
        
        return data

    def serv_data_init(self):   
        serv_data_files = openpyxl.Workbook()
        sdf = serv_data_files.active
        sdf.cell(row=1, column=1).value = "이름"
        sdf.cell(row=1, column=2).value = str(datetime.today().strftime("%Y-%m-%d"))

        for user in self.user_names:
            row = self.data[user]["id"] + 2
            sdf.cell(row=row, column=1).value = user
            sdf.cell(row=row, column=2).value = 0
            sdf.cell(row=row, column=3).value = 0

        serv_data_files.save(self.path_serv_data)

    def serv_data_load(self):
        serv_data_files = openpyxl.load_workbook(self.path_serv_data, read_only=False, data_only=True)
        sdf = serv_data_files.active
        serv_data = dict()

        self.serv_col_num_data = 2
        while True:
            date = sdf.cell(row=1, column=self.serv_col_num_data).value
            if date == None and date != str(datetime.today().strftime("%Y-%m-%d")):
                sdf.cell(row=1, column=self.serv_col_num_data).value = str(datetime.today().strftime("%Y-%m-%d")) + f" {self.day[datetime.today().weekday()]}"
                break
            self.serv_col_num_data = self.serv_col_num_data + 2

        row = 2
        while True:
            if sdf.cell(row=row, column=1).value != None:
                sdf.cell(row=row, column=self.col_num_data).value = 0
                sdf.cell(row=row, column=self.col_num_data + 1).value = 0
                serv_data[us]["early_leave"] = sdf.cell(row=row, column=self.serv_col_num_data).value 
                serv_data[us]["late"] = sdf.cell(row=row, column=self.serv_col_num_data + 1).value 
            else:
                break
            row = row + 1
                
        serv_data_files.save(self.path_serv_data)

        return serv_data

    def schedule_save(self):
        pass

    def schedule_init(self):
        data_files = openpyxl.load_workbook(self.path_data)
        df = data_files.active

        schedule_files = openpyxl.Workbook()
        sf = schedule_files.active
        
        sf.cell(row=1, column=1).value = "이름"
        sf.cell(row=1, column=2).value = "출석 수"
        sf.cell(row=1, column=3).value = "총 결석 수"
        sf.cell(row=1, column=4).value = "결석 수"
        sf.cell(row=1, column=5).value = "지각 수"
        sf.cell(row=1, column=6).value = "조퇴 수"

        for user in self.user_names:
            row = self.data[user]["id"] + 2

            sf.cell(row=row, column=1).value = user
            sf.cell(row=row, column=2).value = self.data[user]["attend_count"]
            sf.cell(row=row, column=3).value = self.sum_absent_count(self.data[user]["absent_count"], self.data[user]["late_count"], self.data[user]["early_leave_count"])
            sf.cell(row=row, column=4).value = self.data[user]["absent_count"]
            sf.cell(row=row, column=5).value = self.data[user]["late_count"]
            sf.cell(row=row, column=6).value = self.data[user]["early_leave_count"]

        schedule_files.save(self.path_schedule)

    def schedule_check_init(self):
        schedule_files = openpyxl.load_workbook(self.path_schedule, read_only=False, data_only=True)
        sf = schedule_files.active

        self.col_num_data = 7
        while True:
            date = sf.cell(row=1, column=self.col_num_data).value
            if date == None and date != str(datetime.today().strftime("%Y-%m-%d")):
                sf.cell(row=1, column=self.col_num_data).value = str(datetime.today().strftime("%Y-%m-%d")) + f" {self.day[datetime.today().weekday()]}"
                break
            self.col_num_data = self.col_num_data + 1
        
        
        row = 2
        while True:
            if sf.cell(row=row, column=self.col_num_data).value != None:
                self.data[str(sf.cell(row=row, column=1).value)]["check_time"] = sf.cell(row=row, column=self.col_num_data).value
            else:
                break
            row = row + 1

        schedule_files.save(self.path_schedule)

    def schedule_check(self, user, time, state):
        
        if state == 1:
            check_time = self.data[user]["check_time"]
            second_day = self.data[user]["second_day"]
            if check_time == None:
                self.data[user]["attend_count"] = self.data[user]["attend_count"] + 1
                self.data[user]["check_time"] = time

            elif check_time != None:
                self.data[user]["check_time"] = self.data[user]["check_time"] + '/' + time
        elif state == 2:
            pass

        elif state == 3:
            pass

        elif state == 4:
            pass

        elif state == 5:
            pass

    def sum_absent_count(self, absent_count, late_count, early_leave_count):
        sum_absent = absent_count + (late_count + early_leave_count) // 3   
        return sum_absent

# att = attendance()
# print(att.data)
