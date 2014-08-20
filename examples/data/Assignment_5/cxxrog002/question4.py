""" graph after been given a function
Roger Cox
    15/04/2014"""


def graph ():
    import math
    # so functions enter can use math
    fx=input("Enter a function f(x):\n")
    
    for y in range (10,-11,-1):
        # the y axis of graph 
        for x in range(-10,11):
            #the x axis of graph
            if(y==round(eval(fx))):
                
                print("o",end="")
             # first priority print o   
            elif y==0 and x==0:
                
                print("+",end="") 
                # then +
                
            elif(y==0):
                # then axis's
                print("-",end="")
                
           
            
            elif x==0 :
                print("|",end="")
            # SPACING OF GRAPH    
            else :
                print(" ",end="")
        #make new line after each inner loop
        print()        
       
graph()