# If the number is positive, we print an appropriate message
#If....Condition
num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")


# Program checks if the number is positive or negative
# If...Else Condition
num = 3

# Try these two variations as well. 
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")


#ELIF...condition

i = 10
j = 20

if i > j:
 print("I is greater")
elif i < j:
 print("J is greater")

 #SAME LINE EXECUTE

i = 20
j = 10

if i > j: print("I is greater")

#ONE LINE IF ELSE STATEMENT

i = 20
j = 30

print("I is greater") if i > j else print("J is greater")

#PASS STATEMENT

i = 20
j = 30

if i == j:
 pass

print("Hello world")