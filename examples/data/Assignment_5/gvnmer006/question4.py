import math

#displayList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
count1=0
def input1():
    func=input("Enter a function f(x):\n")
    func=func.lower()   
    return func 

def plot():
    
    yList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    func=input1()
    func=func.replace("x","(x)")
    for i in range(-10,11):
        x1=str(i)
        yList[(i+10)]=round(eval(str(func.replace("x",x1))))
    for y in range(10,-11,-1):
        displayList=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
        if(y==0):
            for x in range(-10,11):
                if(yList[(x+10)]==0):
                    displayList[(x+10)]="o"
                elif x==0:
                    displayList[(x+10)]="+"
                else:
                    displayList[(x+10)]="-"
        else:
            for i in range(-10,11):
                    #if i==0:
                if -10<=yList[(i+10)]<=10:
                    if yList[(i+10)]==y:
                        displayList[(i+10)]="o"    
                    elif displayList[10]!="o":
                        displayList[10]="|"                          
                    #displayList[10].replace("|","o")    
                
               
        for i in range(21):
            print(displayList[i],end='')    
        print()        
            
        
    
plot()