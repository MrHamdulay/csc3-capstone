#a programe ro determine weather a year is leap or not
#mashau zwivhuya
#7 march 2014
def main():
    year=eval(input("Enter a year:\n"))
    if (year%4)== 0 and (year%100) !=0 or (year%400)==0:
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
main()        