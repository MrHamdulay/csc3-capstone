"""program to draw a text-based graph of function _ refer to Hussein's notes from last term!
Thabiso Beau
15 April 2014"""
import math
def main():
    funksie=input('Enter a function f(x): \n') #asking user to enter the function
    
    for y in range(10, -11,-1): #creating a y-axis
        for x in range (-10, 11): #creating a x-axis
             #convert the function into a number
            f_of_x= round(eval(funksie)) #rounding values so intercepts are whole numbers
            if y == f_of_x:
                print("o", end='') #f(x) will be equal to the entered function
            elif x == 0 and y ==0: #creating the origin
                print('+', end='')
            elif x ==0: #creating condition for printing of x-axis
                print('|', end='')
            elif y ==0: #creating condition for printing of y-axis
                print('-', end='')
            else:
                print(' ', end='') #creating open space in order for the point to be plotted
        print()
main()