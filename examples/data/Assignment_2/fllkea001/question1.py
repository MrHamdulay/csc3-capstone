#Keanon Fell
#PRogram to determine whether or not a year is a leap year
x = eval(input("Enter a year:\n"))
if x%400 == 0: #Checking criteria a
    print(x,"is a leap year.")
elif x%4==0 and x%100!=0: #Checking criteria b
    print(x,"is a leap year.")
else:
    print(x,"is not a leap year.")
    

