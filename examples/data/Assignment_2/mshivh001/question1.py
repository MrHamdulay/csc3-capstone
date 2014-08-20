#A program for determining whether a year is a leap year or not.

def main():
        year = eval(input('Enter a year:\n'))
         
        if year%400==0:
                print(year, "is a leap year.")
        elif year%100==0:
                print(year, "is not a leap year.")
        elif year%4==0:
                print(year, "is a leap year.")
         
        else:
                print(year, "is not a leap year.")
             
main()