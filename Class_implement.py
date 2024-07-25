"""Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Eg.: My class.Myattribute
When we call a method of this object as myobject.method(arg1, arg2), 
this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about. 
"""
class Student:

    
    
    def Inputattr(self):
        self.name = input('my name is')
        self.depart = input('my department is')
        self.status = input('i have ')
    def fun(self):
        print(self.name)
        
        print(self.depart)
        print(self.status)

list=[]

for i in range(0,2):
    a=Student()
    list.append(a)
for i in range(0,2):
    list[i].Inputattr()
for i in range(0,2):
    list[i].fun()