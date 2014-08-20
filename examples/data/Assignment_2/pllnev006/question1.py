# Program to check for leap years
# Nevarr Pillay - PLLNEV006
# 8 March 2014

def leap(year):
    answer = ""
    if(year%400 == 0):
        answer = "is a leap year."
    else:
        if((year%4 == 0) and (year%100 != 0)):
            answer = "is a leap year."
        else:
            answer = "is not a leap year."
            
    return answer

def main():
    year = eval(input("Enter a year:\n"))
    print(year,leap(year))
    
main()    