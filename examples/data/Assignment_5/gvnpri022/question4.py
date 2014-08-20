"""question 4- assignment 5
prinesan govender
14 april 2014"""
import math
#input function
def inputGraph(i , func):
       
    x=i
    yval= round((eval(func)),0)
    #print(yval)
    return yval
#function to draw graph
def drawGraph():
    
    function= input("Enter a function f(x):\n")
       
    # a y loop and x loop to run through each co-ordinatre   
    for y in range(10,-11,-1):
        
        for x in range (-10,11,1):
       
                
            if(y==inputGraph(x, function)):#checking if there is a value at this specific ordered pair
                print("o",end="")
            
            else: #if no value at ordered pair
                if((x==0)and(y!=0)):
                    print("|",end="")
                elif(y==0) and x!=0:
                    print("-",end="")
                elif(y==0 and x==0):
                    print("+",end="")
                else:
                    print(" " ,end="" )                
        print()


def main():
    drawGraph()
if __name__ == "__main__":
    main ()

        


