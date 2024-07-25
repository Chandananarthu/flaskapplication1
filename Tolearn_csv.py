import csv
from datetime import date, datetime
import traceback
import logging

# Configure logging
logging.basicConfig(filename='studentsdata.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

file = open('studentsdata.xlsx', 'a')
file = csv.writer(file)

class Student:
    student = "mtech student"  # Class variable
    
    def __init__(self, name):
        self.name = name
        self.depart = input('My department is: ')
        self.status = input('I have: ')
        
    def __str__(self):
        t = date.today()
        current_time = datetime.now()
        return f"Record {self.name} is entered on date {t} and time is {current_time}"
    
    def fun(self):
        try:
            file.writerow([self.name, self.depart, self.status])
            logging.info(f"record added for {self.name}")
        except Exception as e:
            logging.error(f"failed to write record for {self.name}: {e}")
            print("File can't be written:", traceback.format_exc())

students_list = []

# Driver code - Object instantiation
for i in range(2):  # Changed to 2 for simplicity
    name = input("Enter name: ")
    student = Student(name)
    students_list.append(student)

file.writerow(['Name', 'Department', 'Status'])
for student in students_list:
    print(student)
    student.fun()
