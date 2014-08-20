#Shivam Ragoonaden
#RGNSHI002
#Program that uses recursion to count number of repeated pair of characters in a string

m=input("Enter a message:\n")

def Pairs(m):
    
    if m=="":  #If nothing
        return 0
    elif(len(m)==1):  #Base case, if it's 1 character, there are no repeated pairs 
        return 0
    
    else:
        
        if m[0]==m[1]:  #if it's the same as the next one
            m=m[2:]   #Slice the two characters that are pairs
            return 1+Pairs(m)  #Count +1 and recall the function again
        else:
            return Pairs(m[1:])  #Else recall the function and slice the first character
        
x=Pairs(m)  #Call the function
print("Number of pairs: " + str(x))
    