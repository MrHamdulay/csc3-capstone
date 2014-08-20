year=eval(input("Enter a year:\n"))
def main():
    if (year%400==0 or year%4==0):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.\n")
        
main()