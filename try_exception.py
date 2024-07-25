"""Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors are problems in a program due to which the program will stop the execution. 
On the other hand, exceptions are raised when some internal events occur which change the normal flow of the program.
SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
NameError: This exception is raised when a variable or function name is not found in the current scope.
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module."""
from datetime import date, datetime

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
    try:
        def fun(self):
            file.write(self.name)
            file.write("\t details:\n")
            file.write(self.student)
            file.write("\t")
            file.write(self.depart)
            file.write("\t")
            file.write(self.status)
            file.write("\n")
            file.write("\n")
     
    except IOError:
        print("file cant be written")
    

list=[]

for i in range(0,2):
    name=input("enter name")
    a=Student(name)
    list.append(a)
for i in range(0,2):
    print(list[i])
    list[i].fun()

file.close()
