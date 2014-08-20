#07/03/2014
#Shivaan Motilal
#Programme to determine whether a year is leap year or not



n=eval(input("Enter a year:\n"))
x=n%400

if x%8==0:
    print(n,"is a leap year.")

else: print(n,"is not a leap year.")

    
    
