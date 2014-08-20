#question 4, assignment 5
#Emma Jordi
#15 april 2014

        
def main():

        import math 
        yinc=2/20
        #get input
        function = input("Enter a function f(x):\n")
        
                
        
        for y in range(-10,11):
                for x in range(-10,11):
                        #round off function and evaluate
                        x_real= round(eval(function))
                        y_real= -y
                        #fill in graph
                        if x_real== 0 and y_real==0:
                                print("o", end="") 
                        elif x_real==y_real:
                                print("o",end="")
                        #draw axes
                        elif x == 0 and y==0:
                                print("+", end="")
                        elif x==0 :
                                print("|", end="")
                        elif y==0:
                                print("-", end ="")
                        #fill with spaces
                        else:
                                print(" ", end ="")
                print()

main()
    