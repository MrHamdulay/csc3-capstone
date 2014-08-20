#author: quincy cele
#student number: CLXQUI001
#date 10 march 2014
# this program determines whether a year is a leap year or not
x=eval(input("Enter a year:\n")) 
if x%400==0:
    print(x,"is a leap year.")
elif x%4==0  and x%100 !=0:
    print(x,"is a leap year.")
else:
    print(x,"is not a leap year.")
    