#Tato Moaki MKXTAT001
#Program to draw a text based graph of a mathematical function
#Assignment5 question4
def main():
    
    import math
    function = input("Enter a function f(x):\n")
   
    for y in range(10,-11,-1):
        for x in range(-10,11,1):            
            new_Function = round(eval(function))#compute new value of function for diff values of x
            if(new_Function == y):#print the function where it is equal to y 
                print("o", end="")
            elif(y==0 and x==0): 
                print("+", end="")
            elif(x == 0 and y != 0 and y != new_Function):#print the y axis
                print("|", end="")
            elif(y==0 and  x != 0 and  y != new_Function):#print the x axis
                print("-", end="")
            else:
                if( y != 0):
                    if(x != 0):
                        if(y != new_Function):
                            print(" ", end="")
        print()
        
if __name__ =="__main__":
    main()

