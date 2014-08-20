
import math

function=input("Enter a function f(x):""\n") #ask user for function f(x)
y_coordinates=[]                           #create an Empty list to store values of f(x)
for i in range(-10,11):
    new_function=""                            #New function 
#Calculating and storing values of f(x) into empty list
    for j in function:
        if(j=='x'):
            new_function+='('+str(i)+')'
        else:
            new_function+=j
    y_coordinates.append(eval(new_function))

#Drawing the graph f(x)
for i in range(10,-11,-1):  #
    for j in range(-10,11):
        if(round(y_coordinates[j+10])==i): #plot the points
            print('o',end='')
        elif(i==0 and j==0):   #plot the origin
            print('+',end='')        
        elif(i!=0 and j==0):    #y axis
            print('|',end='')
        elif(i==0 and j!=0):    #x axis
            print('-',end='')
        else:
            print(' ',end='')
    print()