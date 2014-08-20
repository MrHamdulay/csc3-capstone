#24 march 2014
#sarayn subroyen

def tri():
    h = eval(input("Enter the height of the triangle:\n"))
    
    for i in range(1,h+1): #h is the height
        a = h - i          # a is the spaces
        print(a*" ","*" * i,"*" * (i-1), sep="")
        
tri()
    