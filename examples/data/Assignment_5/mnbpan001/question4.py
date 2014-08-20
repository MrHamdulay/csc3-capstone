"""Program to plot graph of a function
Author: Pankaj Munbodh
16 April 2014"""


import math
function=input("Enter a function f(x):\n")

#create graph using nested loop. Reverse direction of corrdinates for y-axis.
for j in range(10,-11,-1):
    for i in range(-10,11):
        x=i
        function1=eval(function) # since function is a string, it must be evaluated after a value is given to x.       
        
        #continue statements are used to construct axes and cater for exceptions
        # A range of ycoordinate-0.5<=function<ycoordinate+0.5 is used to decide if point is plotted
        if i==0 and j==0:
                    if -0.5<=function1<0.5:
                        print("o",end='')
                    else:
                        print('+',end='')
                    continue        
        if i==0:
            if j-0.5<=function1<j+0.5:
                print("o",end='')
            else:
                print('|',end='')
            continue
        if i==10 and j==0:
            if -0.5<=function1<0.5:
                print("o")
            else:
                print('-')
            continue
        if i==10:
            if j-0.5<=function1<j+0.5:
                print("o")
            else:
                print(' ')
            continue
        if j==0:
            if -0.5<=function1<0.5:
                print("o",end='')
            else:
                print('-',end='')
            continue
        
        # if-else statement used to construct empty space and graph, it is the mostly used part in this program.
        if j-0.5<=function1<j+0.5:
            print("o",end='')
        else:
            print(' ',end='')
        