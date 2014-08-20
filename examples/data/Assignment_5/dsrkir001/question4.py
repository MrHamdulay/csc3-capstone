#program to draw a text-based graph of a mathematical function f(x)
#Kiran Desraj - DSRKIR001
#12 April 2014


import math 
#create empty list which will be used to keep y-values 
ordinate = []
function = input("Enter a function f(x):\n")  

 
for a in range(-10,11):   #axis limits of -10 to 10
    
    c = ''  #Variable created to compute graph
    
    for b in function:       #determine function values
        if( b == 'x'):
            c = c +'('+str(a)+')'
        else:
            c = c + b
            
    ordinate.append(eval(c))

for a in range(10,-11,-1):   #to graphically plot function
    for b in range(-10,11):
        if(round(ordinate[b+10])==a):
            print('o',end='')
        elif(a==0 and b!=0):
            print('-',end='')
        elif(b==0 and a!=0):
            print('|',end='')
        elif(a==0 and b==0):
            print('+',end='')           
        
        else:
            print(' ',end='')
    print()   