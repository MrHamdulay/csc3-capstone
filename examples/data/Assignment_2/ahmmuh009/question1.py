#question 1 
#re-write this stuff here

def leap_year():
    
    enter_year=eval(input("Enter a year:\n"))
    
    if enter_year%400==0:
        print (enter_year,"is a leap year.")
    elif enter_year%4==0 and enter_year%100!=0:
        print (enter_year,"is a leap year.")
    else:
        print (enter_year,"is not a leap year.")
        
leap_year()