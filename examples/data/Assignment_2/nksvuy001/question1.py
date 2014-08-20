#program to work out whether year is leap or not
#vuyolwethu nkosi
#8 march 2014

leap=eval(input("Enter a year:\n"))
if(leap%400==0 or leap%4==0 and leap%100!=0):
    print(leap,"is a leap year.")
else:print(leap,"is not a leap year.")
