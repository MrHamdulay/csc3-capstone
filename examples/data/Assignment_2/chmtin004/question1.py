#Program to work out if a year is a leap year
#Tinotenda Chemvura (CHMTIN004)
#08 March 2014

#___________________Program starts here_____________________________*
def work_out_leapyear():        #defining the function to work out leap years
    year=eval(input("Enter a year:\n")) #prompt user to enter a year
    if year%400==0 or (year%4 == 0 and year%100!=0):#conditions for a leap year
        print(year,"is a leap year.")
    else: print(year,"is not a leap year.")

work_out_leapyear()