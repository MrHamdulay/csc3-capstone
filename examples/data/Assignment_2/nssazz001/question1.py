#program to determine leap year
#Azza Nassor
#NSSAZZ001

x=eval(input("Enter a year:\n"))
y= x%400
z= x%4
s= x%100

if y == 0 or (z == 0 and s!= 0):
    print (x, "is a leap year.")
else:
    print (x, "is not a leap year.")

       