#Nicholas Mazower, MZWNIC001
#18/04/2014
#Graphing Program

import math
function=input("Enter a function f(x):\n")
#The overly large string is the graph template i.e the cartesian plane. The String could be compressed but the programmer did not think of that before finishing it.
cartesian="          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"----------+----------\n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"+"          |          \n"

x_coord=0
#b_lin is the one behind the linear coordinate.
b_lin=0
#lin is the linear coordinate as the program works by converting the x and y coordinates to a single value linear coordinate
lin=0
for x in range (-10,11):
    y=eval(function)
    y=round(y)
    if y>10 or y<-10:
        pass
    elif y>0:
        lin=x_coord+(10-y)*22 + 1
        b_lin=lin-1
        cartesian=cartesian[:b_lin]+"o"+ cartesian[lin:]
    elif y==0:
        lin=x_coord+221
        b_lin=lin-1
        cartesian= cartesian[:b_lin]+"o"+ cartesian[lin:]
    elif y<0:
        lin=x_coord+(10+abs(y))*22 + 1
        b_lin=lin-1
        cartesian= cartesian[:b_lin]+"o"+ cartesian[lin:]
    x_coord=x_coord+1
    lin=0

print(cartesian)