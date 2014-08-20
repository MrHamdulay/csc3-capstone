#Program to calculate if a year is leap year or not.
#Siphesihle Cele
#17 March 2014

year =eval(input("Enter a year:\n"))    #getting input from the user

if year%4==0 and year%100!=0 or year%400==0:  #checking the condition
    
    print(year,"is a leap year.")  #print statement if it meets the conditions
    
else:
    print(year,"is not a leap year.")
    