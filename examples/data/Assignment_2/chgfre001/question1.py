#program to determine whether a year is a leap year
#11 march 2014
#by frederick chigwaza

def leap_year():
    year = eval(input("Enter a year:\n"))
    if (year%400==0):
        print(year,"is a leap year.")
    elif(year%4==0 and year%100!=0):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
    
leap_year()        
        
        
        
      
        
        
