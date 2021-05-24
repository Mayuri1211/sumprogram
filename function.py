#functions

def showMessage(): 
  print("This is function") 
print("Hello from Python") 
print("Call function by its name") 
showMessage()



#FUNCTION PARAMETER 
def showMessage(name): 
 print("Your name is " + name) 
 print("Call function by its name") 
showMessage('John')

#DEFAULT PARAMETER VALUE 
def showMessage(name='Default name', age=30):
     print("Your name is " + name + " Age is ", age) 
print("Call function by its name") 
showMessage()

#PASS ONE PARAMETER  
def showMessage(name='Default name'): 
 print("Your name is " + name) 
print("Call function by its name") 
showMessage()

#PASSING A LIST AS AN ARGUMENT 
def showList(lang): 
 for x in lang: 
  print(x) 
lang = ["HTML", "CSS", "Bootstrap", "Java"] 


