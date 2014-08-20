#Assignment 2
#Question 1
#determining a leap year.

def leapyear():
    year = eval(input("Enter a year:\n"))
    test = year/4
    if round(year/400)==year/400:
        print(year,"is a leap year.")
    else:
        if round(year/100)!=year/100:
            if round(test)==test:
                print(year,"is a leap year.")
            else:
                print(year,"is not a leap year.")
        else:
            print(year,"is not a leap year.")
    
    
leapyear()