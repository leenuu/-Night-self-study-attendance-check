from datetime import datetime
import openpyxl
import os

class attendance:
    def __init__(self):
        self.day = ['월', '화', '수', '목', '금', '토', '일']
        self.path_data = os.path.join(os.getcwd(), 'data.xlsx')
        self.path_schedule = os.path.join(os.getcwd(), 'schedule.xlsx') 
        self.col_data = 0
        self.user_names = list()
        self.data = self.data_load()
        
        self.schedule_init()
        # try:
        #     self.schedule_check_init()

        # except FileNotFoundError:
        #     self.schedule_init()
        #     self.schedule_check_init()

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

    def data_save(self):
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
        pass

    def schedule_check(self, users):
        pass
    
    def sum_absent_count(self, absent_count, late_count, early_leave_count):
        sum_absent = absent_count + (late_count + early_leave_count) // 3   
        return sum_absent

att = attendance()
# print(att.data)