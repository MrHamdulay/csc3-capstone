x= eval(input("Enter a year:\n"))
t= 0

a = x%400
b = x%4
c = x%100

if a == 0:
    t=1
    
if (b == 0):
    if(c != 0):
        t=1
        
if (t==0):
    print(x,"is not a leap year.")
else:
    print(x,"is a leap year.")