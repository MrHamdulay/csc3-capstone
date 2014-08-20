#Assignment 2, Question 1
#leapYear Assignment
#Kieran Reilly  
#RLLKIE001  
#10/03/14

year = 0
year = eval(input("Enter a year: \n"))

test = year / 4                 #test used to check the factor four
test = round(test)
test = float(test)              #if rounded float != year, year has remainder, not a leap year

test2 = year / 400
test2 = round(test2)
test2 = float(test2)            #test 2 represents the 400 factor test

test3 = year / 100
test3 = round(test3)
test3 = float(test3)            #test3 represents the 100 factor test


if(test2 == (year/400)):
        print(str(year)+" is a leap year.")
elif(test3 == (year/100)):
        print(str(year)+" is not a leap year.")
elif(test == (year/4)):
        print(str(year)+" is a leap year.")
else:
        print(str(year)+" is not a leap year.")