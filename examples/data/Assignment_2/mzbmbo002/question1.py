#Mbongeni Mazibuko
#MZBMBO002
#Assignment 2

x = eval(input('Enter a year:\n'))

def leap(year):
    if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
        print(year, 'is a leap year.')
    else : print(year, 'is not a leap year.')
    
leap(x)