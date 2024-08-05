import logging
import argparse
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
        self.id = id
        self.guide = guide

    def fun(self):
        logging.info("Name: %s", self.name)
        logging.info("Department: %s", self.department)
        logging.info("%s's student ID is %s", self.name, self.id)
        logging.info("Project guide is %s", self.guide)



if __name__ == "__main__":
    start = datetime.datetime.now()
    parser=argparse.ArgumentParser(description="script for displaying details")
    parser.add_argument("id", type=str)
    parser.add_argument("guide", type=str)
    args = parser.parse_args()
    id=args.id
    guide=args.guide
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
   