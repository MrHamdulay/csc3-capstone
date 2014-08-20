"""assignment 5
question4
mphuthi mamorena
16 april 2014"""

import math

def graph():
    f=input("Enter a function f(x):\n")
    for y in range(10,-11,-1):
        for x in range(-10,11):
            b=round(eval(f))# turning f into an int for calculations
            if y==b:
                print('o',end='') # printing where f is defined
            elif x==0 and y==0:
                print('+',end='')# creating the origin
            elif y==0:
                print('-',end='')# creating the x axis
            elif x==0:
                print('|',end='') # creating the y x axis
            else:
                print(' ',end='')
        print()
graph()