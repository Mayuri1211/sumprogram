#create first class
class FirstClass:
    i = 10
j = 5

print(FirstClass)

#create first object
class FirstClass:
  i = 20


demo1 = FirstClass()

print("Value from Class" ,demo1.i)



#init() function
class User:
    def __init__(self, name, contact):
      self.name = name;
      self.contact = contact

user = User("Welcome to World", 20)

print(user.name)
print(user.contact)



