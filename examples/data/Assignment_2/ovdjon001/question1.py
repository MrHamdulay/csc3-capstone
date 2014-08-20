def main():
    year = eval(input("Enter a year:"))
    print()
    if isLeapYear(year):
        print(year, "is a leap year.")
    else:
        print(year,"is not a leap year.")
 
def isLeapYear(year):
    if year%400 == 0:
        return True
    elif year% 4 ==0 and year%100!=0:
        return True
    else:
        return False


main()
    
