"""# Class and Instance Variables 
Instance variables are for data, unique to each instance and class variables are for attributes and methods shared by all instances of the class. Instance variables are variables whose value is assigned inside a constructor or metho
    d with self whereas class variables are variables whose value is assigned in the class."""
from datetime import date, datetime
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
        print(self.name)
        print(self.student)
        print(self.depart)
        print(self.status)

list=[]
for i in range(0,2):
    name=input("enter name")
    a=Student(name)
    list.append(a)
for i in range(0,2):
    print(list[i])
    list[i].fun()
