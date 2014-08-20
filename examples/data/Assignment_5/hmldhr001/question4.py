
#Dhriven Hamlall

import math

def enter():
    function=input("Enter a function f(x):\n")
    function=function.lower()   
    return function 

#=====================================================================================================

def plot_graph():
    
    y_value_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    function=enter()
    function=function.replace("x","(x)")
    
    for i in range(-10,11):
        y_value_list[(i+10)]=round(eval(str(function.replace("x",str(i)))))
        
    for y in range(10,-11,-1):
        Display=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
        if(y==0):
            for x in range(-10,11):
                if(y_value_list[(x+10)]==0):
                    Display[(x+10)]="o"
                elif x==0:
                    Display[(x+10)]="+"
                else:
                    Display[(x+10)]="-"
        else:
            for i in range(-10,11):
                if -10<=y_value_list[(i+10)]<=10:
                    if y_value_list[(i+10)]==y:
                        Display[(i+10)]="o"    
                    elif Display[10]!="o":
                        Display[10]="|"                          
                      
#===========================================================================================================                
               
        for i in range(21):
            print(Display[i],end='')    
        print()        
            
        
    
plot_graph()