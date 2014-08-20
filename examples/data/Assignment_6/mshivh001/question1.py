#MAISHA IVHA
#21/04/2014
#PROGRAMME THAT PRINT RIGHT-ALIGNED LIST

def strr():
    y=[]    
    s=input("Enter strings (end with DONE):\n")
    while s!="DONE": 
        y.append(s)
        s=input() 
    if y!=[]:
        s=max(y,key=len) #finding the longest string
        n=len(s) #finding the lenght of the longest string
        m=" "

        print("\nRight-aligned list:")   
        for i in y:
            print(m*(n-len(i))+i)#a loop that iterates for every character in a loop 
                                 
            
    else:
        print("\nRight-aligned list:") #string that is printed if the list is empty
    
strr()