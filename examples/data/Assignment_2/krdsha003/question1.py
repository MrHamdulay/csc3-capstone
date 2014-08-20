#Question 1
#Name: Shaheen Karodia
#Student number: KRDSHA003
#2014-03-08

#Caluating Leap Year

year=eval(input("Enter a year:\n"))    

if year%400==0 :
    print(year,"is a leap year.") 

elif year%4==0 and year%100!=0 :
    print(year,"is a leap year.\n") 
else:
    print(year, "is not a leap year.")