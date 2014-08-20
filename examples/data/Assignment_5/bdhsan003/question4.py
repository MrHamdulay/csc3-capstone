#bdhsan003
import math

funct=input("Enter a function f(x):""\n") 
y_co=[]  #creating an empty list
for k in range(-10,11):
    new_funct=""  #New function 

    for p in funct:
        if(p=='x'):
            new_funct=new_funct+'('+str(k)+')'
        else:
            new_funct=new_funct+p
    y_co.append(eval(new_funct))


      #To draw the graph
for k in range(10,-11,-1):  
    for p in range(-10,11):
        if(round(y_co[p+10])==k): 
            #for the points to be plotted
            print('o',end='')
        elif(k==0 and p==0):   
            #to plot the origin
            print('+',end='')        
       
        elif(k!=0 and p==0):    
            
            print('|',end='')
       
        elif(k==0 and p!=0):    
            
            print('-',end='')
        else:
            print(' ',end='')
    print()