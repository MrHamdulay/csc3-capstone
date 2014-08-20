# Determine whether a year is a leap year

x=eval(input("Enter a year:\n"))
#this is evaluating if year is divisible by 400
#x//400
rem=x%400
rem2=x%4
rem3=x%100

#<rem has no remainder> or <rem 2 has no remainder AND rem3 has a remainder>
if (rem==0) or (rem2==0) and (rem3!=0):
    print(x ,"is a leap year.")
else:
    print(x ,"is not a leap year.")
    
    
