# Karabo Choma
#March 14
#Leap year check
def leap():
    year=eval(input("Enter a year:" '\n'))
    if year%400==0 :
        print(year, "is a leap year.")
    elif year%4==0 and year%100 :
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

leap()