# Graph Plotter
# Khwezi Majola
# MJLKHW001
# 14 April 2014

def plot():
    import math
    x = input('Enter a function f(x):\n')
    for y in range(10, -11, -1):
        for k in range(-10, 11):
            if '**' in x:
                j = abs(k)
            else: j = k
            kval = round(eval(x.replace('x', str(j))))
            if y == kval:
                print ("o",end="")            
            elif k == 0 and y == 0:
                print ("+",end="")               
            elif k == 0:
                print ("|",end="")
            elif y == 0:
                print ("-",end="")            
            else:
                print (" ",end="")  
        print()
plot()