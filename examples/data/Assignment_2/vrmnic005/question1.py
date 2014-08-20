#VRMNIC005
#assignment 2

def leapyear():
    year = eval(input("Enter a year: \n"))
    if year%400 == 0:
        print (year, " is a leap year.", sep = "")

    elif(year%4 == 0) and (year%100 != 0):
        print (year, " is a leap year.", sep = "")

    else:
     print (year, " is not a leap year.", sep = "")

leapyear()
