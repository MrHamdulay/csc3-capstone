a=eval(input("Enter a year:\n"))
def year(a):
    if a%400==0 or (a%4==0 and a%100!=0):
        print(a,"is a leap year.")
    else:
        print(a,"is not a leap year.")
year(a)