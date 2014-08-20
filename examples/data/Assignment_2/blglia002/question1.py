year = eval(input("Enter a year:\n"))
if (year%4==0) and (year%100!=0): #this gives the remainder of the year. i.e, if the remainder is equal to 0, then....
    print(year,"is a leap year.")
elif (year%400==0):
    print(year,"is a leap year.")
else: print(year,"is not a leap year.")    

#Liam Blignaut
#How to determine a leap year.
#08/03/2014