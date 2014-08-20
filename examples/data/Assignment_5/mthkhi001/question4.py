import math

# get user defined function
function = input("Enter a function f(x):\n")

yline = 10
for y in range (-10,11):
    line = ""
    for x in range (-10,11):
        xsafety = function.replace('x','(x)')
        ycoordinate = eval(xsafety.replace('x',str(x)))
        #print ("y" + str(ycoordinate))
        #print("yline" + str(yline))        
        if  ((yline -1)< round(ycoordinate) <= yline):
            line = line +"o"
            
        elif y == 0 and x == 0:
            line = line + "+"
            
        elif y == 0:
            line = line + "-"
            
        elif x == 0:
            line = line + "|"
            
        else:
            line = line + " "
    print(line)              
    yline = yline- 1
        
