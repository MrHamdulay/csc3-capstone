#Write a program to determine whether a year is a leap year or not. A year is a leap year if (a) it is divisible by 400 or (b) it is divisible by 4 but not by 100.
#EMMANUEL NJABULO MAJOZI
#MJZEMM001

def main():
    year = int(input("Enter a year: \n"))
    year1 = year %400
    year2 = year%4
    year3 = year%100
    
    if year1 == 0 and year3 == 0:
        print (year,"is a leap year.")
    elif year2 == 0 and year3 != 0 :
        print (year,"is a leap year.")
    else:
        print (year,"is not a leap year.")
main()