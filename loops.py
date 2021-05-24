#while Loop

i=1    
number=0    
b=9    
number = int(input("Enter the number:"))    
while i<=10:    
    print("%d X %d = %d \n"%(number,i,number*i))    
    i = i+1   

#FOR LOOPS

i = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']

for values in i:
  print(values)

  #RANGE

for i in range(1,10):
  print(i)

#Break
  str = "python"  
for i in str:  
    if i == 'o':  
        break  
    print(i);

 #NEsted For Loop   
rows = int(input("Enter the rows:"))  
 
for i in range(0,rows+1):  
 
    for j in range(i):  
        print("*",end = '')  
    print()    