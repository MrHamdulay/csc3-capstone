#linear graph
#Katlego Gaveni
#15th April 2014



import math

def graph(fx):
    for y in range(10,-11,-1):             #y-axis range
        for x in range (-10,11):           #x-axis range
            if(eval(fx) == y):
                print("o", end = "")       #drawing of graph points
            elif(x == 0 and y == 0):       #origion of graph
                print("+", end = "")
            elif y==0 :     
                print("-",end="")         #drawing of x-axis
            elif(x == 0):
                print("|", end = "")      #drawing of y-axis
            elif(eval(fx) != y):
                print(" ", end = "")
                        
        print()

    
def main():
    fx=input("Enter a function f(x):\n") #user selcting graph, which will later be evaluated by th eval function in the graph(fx)
    graph(fx)

main()    
    
    
    
    
    
    
    
    
    
    
    


