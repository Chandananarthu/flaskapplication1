from datetime import date, datetime
import traceback
file = open('recordodmtechstudents.txt', 'a')
class Student:

    
    student="mtech student"
    def __init__(self,name):
        self.name = name
        self.depart = input('my department is')
        self.status = input('i have ')
    def __str__(self):
        t=date.today()
        curenttime= datetime.now()
        return f" record {self.name} is entered on date {t} and time is {curenttime} "
    
    def fun(self):
        try:
            file.write(self.name1)
            file.write("\t details:\n")
            file.write(self.student)
            file.write("\t")
            file.write(self.depart)
            file.write("\t")
            file.write(self.status)
            file.write("\n")
            file.write("\n")
     
        except:
           print("file cant be written", traceback.format_exc())
    

list=[]

for i in range(0,2):
    name=input("enter name")
    a=Student(name)
    list.append(a)
for i in range(0,2):
    print(list[i])
    list[i].fun()
    

file.close()
