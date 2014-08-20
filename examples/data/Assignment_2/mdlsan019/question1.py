#Name:Sanele Mdlalose
#Student no:MDLSAN019
#Date:08 March 2014
#Question1

def leapyear():                     
    year=eval(input("Enter a year:\n"))
    if (year%400)==0 or ((year%4)==0 and (year%100)!=0):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
leapyear()          