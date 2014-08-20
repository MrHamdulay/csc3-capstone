#Awande Madonsela
#MDNAWA001
#07 March 2014

def leapyear(year):
    if ((year%400==0) or (year%4==0) and (year%100!=0)):
            print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
        
year=eval(input("Enter a year:\n"))
leapyear(year)
          
    