n = eval(input("Enter a year:\n"))
if(n%100!=0 and n%4==0 or n%400==0):
    print(""+str(n)+" is a leap year.")
else:
    print(""+str(n)+" is not a leap year.")
