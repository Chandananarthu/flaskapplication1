import logging

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
        self.id = input("Enter ID: ")
        self.guide = input("Enter guide: ")

    def fun(self):
        logging.info("Name: %s", self.name)
        logging.info("Department: %s", self.department)
        logging.info("%s's student ID is %s", self.name, self.id)
        logging.info("Project guide is %s", self.guide)


# Example usage
if __name__ == "__main__":
    # Creating an instance of Mtechstudent
    a = Mtechstudent('Mtech', 'lh4', 'chandana')
    
    # Logging display information
    logging.info("Displaying student information:")
    a.display()
    
    # Logging fun information
    logging.info("Displaying student fun information:")
    a.fun()
