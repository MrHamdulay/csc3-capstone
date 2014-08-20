#Graph Draw
#James Godlonton  
#12 April 2014

import math

def main():
    func=input("Enter a function f(x):\n")
    for y in range (-10,11):
        ax=y*-1
        line=""
        for x in range (-10,11):
            x/1
            val=eval(func.replace("x","("+str(x)+")"))
            
            if round(val)==ax:
                line=line+"o"
                
            elif ax==0 and x==0:
                line=line+"+"
            elif ax==0:
                line=line+"-"
                
            elif x==0:
                line=line+"|"
            else:
                line=line+" "
                
        print(line)
        
if __name__ == "__main__":
    main()