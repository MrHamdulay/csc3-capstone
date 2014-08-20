import math
#Graph
def graph():
    function=input("Enter a function f(x):\n")
    for y in range (10,-11,-1):
        for x in range (-10,11):
            new_y=eval(function)
            
            if round(new_y)==y:
                print('o',end='')
            elif x==0 and y==0:
                print("+",end='')
            elif y==0:
                print("-",end='')
                #if x==10:
                    #print('')  
            elif x==0:
                print("|",end='')
            #elif x==10:
             #   print('')
            else:
                print(" ",end='')
        print()
#y axis
#x axis
#Enter function
graph()
