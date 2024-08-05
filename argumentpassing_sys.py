'''The sys module provides functions and variables to manipulate Python’s runtime environment. 
Through sys.argv arguments are passed from the command line to the Python script,
However this module, requires the user to know exactly what is required, the type of arguments, and the order in which the program expects them.

This application will accept any input and fail at runtime if the inputs aren't correct'''
import logging
import sys
import datetime
import time
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Student:
    university = "uoh"

    def __init__(self, department, hostelno):
        self.department = department
        self.hostelno = hostelno

    def display(self):
        logging.info("University: %s", self.university)
        logging.info("Department: %s", self.department)
        logging.info("Hostel Number: %s", self.hostelno)


class Mtechstudent(Student):
    def __init__(self, department, hostelno, name):
        super().__init__(department, hostelno)
        self.name = name
        self.id = sys.argv[1]
        self.guide = sys.argv[2]

    def fun(self):
        logging.info("Name: %s", self.name)
        logging.info("Department: %s", self.department)
        logging.info("%s's student ID is %s", self.name, self.id)
        logging.info("Project guide is %s", self.guide)



if __name__ == "__main__":
    start = datetime.datetime.now()
    a = Mtechstudent('Mtech', 'lh4', 'chandana')
    
    logging.info("Displaying student information:")
    a.display()
    time.sleep(3)
    logging.info("Displaying student fun information:")
    a.fun()
    end = datetime.datetime.now()

    # get execution time
    elapsed_time = end-start
    print('Execution time:', elapsed_time, 'seconds')
   