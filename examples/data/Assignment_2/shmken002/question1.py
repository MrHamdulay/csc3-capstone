#Program to tell user whether leap year or not
#kenneth shimabukuro
#12/03/14
def main():
    year = eval(input("Enter a year:\n"))
    if year%400 == 0 or year%4 == 0 and year%100 !=0:
        print(year, "is a leap year.")
    else: print(year, "is not a leap year.")
main()
