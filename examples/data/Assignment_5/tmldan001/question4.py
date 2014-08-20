'''Program to draw a text-based graph of a mathematical function f(x)
Daniel M. Tamale
TMLDAN001
2014-04-16'''

'''To import math library'''
import math

fx=20
def function():
    fx=input('Enter a function f(x):\n')
    '''Setting graph boundaries'''
    for y in range(10,-11,-1):
        for x in range(-10,11):
            
            '''Evaluating the given function and plotting graph'''
            if y==round(eval(fx)):
                print ('o',end='')          
            elif x==0 and y==0:
                print ('+',end='')
            elif x==0 and y!=0:
                if y==round(eval(fx)):
                    print ('o',end='')
                else:
                    print ('|',end='')
            elif y==0 and x!=0:
                print('-',end='')
            else:
                print(' ',end='')
        print()
function()