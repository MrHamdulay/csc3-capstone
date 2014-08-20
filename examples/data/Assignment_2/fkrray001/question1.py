# Author : Rayaan Fakier FKRRAY001
# Date : 07 - 03 - 2014

# Define main function
def main():
    year = int(input("Enter a year:\n"))
    # If statement to check for leap year
    if (year % 400 == 0) or (year % 4 == 0 and year %100 != 0): 
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
   
    
main()
    