x=eval(input("Enter a year:\n"))
a= x%400
b= x%4
c= x%100
if a==0 or (b==0 and c>0): 
    print(x, "is a leap year.")
else:
    print(x, "is not a leap year.")
