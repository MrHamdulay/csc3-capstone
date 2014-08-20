import math

def graph():
    graph = input("Enter a function f(x):\n")
    for y in range(10,-11,-1):
        for x in range(-10,11):
            f_x=round(eval(graph))
            if y ==f_x:
                print("o",end="")
            elif x==0 and y!=f_x and y!=0:
                print("|",end="")
            elif y==0 and y!=f_x and x!=0:
                print("-",end="")
            elif y==0 and x == 0 and f_x!=y:
                print("+",end="")
            else:
                print(" ",end="")
        print()
                
graph()