#MODIFY OBJECT PROPERTIES

class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department

        
obj = Student("Bicky Newton", "IT")

del obj.department 

arr = []
  
# input values to list
arr = [12, 3, 4, 15]
  

ans = sum(arr)
  

print ('Sum of the array is ',ans)
  