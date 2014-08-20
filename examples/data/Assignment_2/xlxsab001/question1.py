x=eval(input("Enter a year:\n"))
y=400.0
z=4.0
w=x%y
d=x%4.0
e=x%100
if (w == 0):
    print(x,"is a leap year.")
    
elif (d == 0) and (e != 0) :
    print(x,"is a leap year.")
    
else:
    print(x,"is not a leap year.")