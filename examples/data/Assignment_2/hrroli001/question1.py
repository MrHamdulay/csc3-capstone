# Assignment 1 - Question 1
# Oliver Harrison - HRROLI001
# 08 March 2014

def main():
    year=eval(input("Enter a year: \n"))
    rem1=year%400
    rem2=year%4
    rem3=year%100
    if rem1==0 or rem2==0 and rem3!=0:
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
        
main()