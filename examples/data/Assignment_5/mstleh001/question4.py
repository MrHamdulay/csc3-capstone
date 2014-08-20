import math

#Lehlogonolo Masetla

def calculateY(f,x):
    return eval(f)
    
def sketchGraph():
    
    f = input('Enter a function f(x):\n') #asks user for input
    
    yinc = 10/20
    
    for y in range(-10,11):
        for x in range(-10,11):
            x_real = x
            y_real = -y
            if  y_real-yinc <= calculateY(f,x_real) <= y_real+yinc:
                
                print('o',end='')          
            elif y_real == 0 and x_real == 0:
                print('+',end='')
            elif y_real == 0 :
                print('-',end='')
            elif x_real == 0 :
                print('|',end='')
            else :
                print(' ',end='')
        print()    

sketchGraph()