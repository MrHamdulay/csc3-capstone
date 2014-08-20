import math

func = input("Enter a function f(x):\n") #prompts for input of mathematical function

for y in range(-10,11): #y axis from -10 to 10
    for x in range(-10,11): #x axis from -10 to 10
        y_real = -y 
        x_real = -x #flipping axes
        if y_real == round(eval(func)):
            print("o", end="") 
        elif x_real == 0 and y_real == 0:
            print('+',end='') #point for cartesian co-ordinates (0,0)
        elif x_real == 0:
            print('|',end='') #line for y axis
        elif y_real == 0:
            print('-',end='') #line for x axis
        else:
            print(" ", end="") #blank spaces
    print() 
        