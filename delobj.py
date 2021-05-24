#delete object property
class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department

        
obj = Student("Bicky Newton", "IT")

del obj.department  