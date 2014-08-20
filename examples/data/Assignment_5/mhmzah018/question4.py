"""assignment 5 - question 4
zaheer mahmood
16-4-2014"""

#import library for functions
import math
y_inc = 1/20

#draw graph
def get_graph(f):
    for i in range(-10,11):
    
        for j in range(-10,11):
            if f.find("**") == True or f.find("**")==0:
                if j<0:
                    j = -j
            funct_store= "("+str(j)+")"
            new_x = f.replace("x", funct_store)
      
            new_x = eval(new_x)
            
            x_real=new_x/10
            y_real=-i/10            
            if y_real - y_inc <= x_real <= y_real + y_inc:
                        print("o", end="")            
                    
        
            elif i==0 and j==0:
                print("+",end="")            
            elif j == 0:
                print("|",end="")
            elif i == 0:
                print("-",end="")
                                        
            else:
                print(" ",end="")
        print()
            
if __name__ == "__main__":
    
#get input from user
    function = input("Enter a function f(x):\n")
    get_graph(function)



    
    
     