#mahdi marcus

s = input("Enter a message:\n") #get input

def repeat(s): 
    
    if s=="": #no message
        return 0
    elif len(s)==1: #one letter
        return 0
    
    else:
        if s[0]==s[1]: #1st char = 2nd char
            s=s[2:] 
            return 1 + repeat(s)
            
        else:
            return repeat(s[1:])
        
print("Number of pairs:", str(repeat(s))) #show the answer

    

    
