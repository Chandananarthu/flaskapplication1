"""__init__(self,name)
The __init__ method is similar to constructors in C++ and Java. Constructors are used to initializing the object’s state. 
Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. 
It runs as soon as an object of a class is instantiated. 
The method is useful to do any initialization you want to do with your object."""
class Student:

    def __init__(self,name):
        self.name = name
        self.depart = input('my department is')
        self.status = input('i have ')

    def fun(self):
        print(self.name)
        
        print(self.depart)
        print(self.status)

list=[]
for i in range(0,2):
    name=input("enter name")
    a=Student(name)
    list.append(a)
for i in range(0,2):
    list[i].fun()