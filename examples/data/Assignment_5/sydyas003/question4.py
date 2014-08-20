import math

f_x=input("Enter a function f(x):\n") #User enters f(x)
y_values=[]#Empty list to store values of f(x)
for i in range(-10,11):
    g_x=""#New function to be evaluated
    #Calculating and storing values of f(x)
    for j in f_x:
        if(j=='x'):
            g_x+='('+str(i)+')'
        else:
            g_x+=j
    y_values.append(eval(g_x))

#Compute graph
for i in range(10,-11,-1):  
    for j in range(-10,11):
        if(round(y_values[j+10])==i):
            print('o',end='')
        elif(i==0 and j!=0):
            print('-',end='')
        elif(i!=0 and j==0):
            print('|',end='')
        elif(i==0 and j==0):
            print('+',end='')
        else:
            print(' ',end='')
    print()