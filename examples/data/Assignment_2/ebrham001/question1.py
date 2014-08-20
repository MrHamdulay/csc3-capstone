# CSC1015F Assoignment 2 - question1.py 
# Hamza Ebrahim



year = eval(input("Enter a year:\n"))
if (year%400==0) or (year%100!=0 and year%4==0): 
    print(year,"is a leap year.")
    
else:
    print(year, "is not a leap year.")  
