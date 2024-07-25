"""__str__() method
Python has a particular method called __str__(). that is used to define how a class object should be represented as a string. It is often used to give an object a human-readable textual representation, which is helpful for logging, debugging, or showing users object information. When a class object is used to create a string using the built-in functions print() and str(), the __str__() function is automatically used. 
You can alter how objects of a class are represented in strings by defining the __str__() method"""
class Student:

    def __init__(self,name):
        self.name = name
        self.depart = input('my department is')
        self.status = input('i have ')


    def __str__(self):
        return f" record {self.name} is entered"
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
    print(list[i])
    list[i].fun()
