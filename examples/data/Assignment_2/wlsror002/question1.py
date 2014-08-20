Year=eval(input("Enter a year: \n"))


def main(Year):
    
    
    remainder_1 = Year%400
    remainder_2 = Year%4
    remainder_3 = Year%100
    if remainder_1 and remainder_2 !=0:
        print(Year,"is not a leap year.")
    elif remainder_2 == 0 and remainder_3 == 0:
        print(Year,"is not a leap year.") 
    elif remainder_1 or remainder_2 ==0:
        print(Year,"is a leap year.")
main(Year)