
def encryption(string):
    
    if string[0]==" ":
        
        return " "+encryption(string[1:])
    
    elif (string[0]==string[len(string)-1]): 
        
        if string[0].islower(): 
            
            if string[0]=="z": 
                
                return "a"
            else:
                return chr(ord(string[0])+1)
        else:
            return string[0]
        
    elif string[0].islower(): 
        
        if string[0]=="z":
            
            return "a"+encryption(string[1:])
        
        else:
            return chr(ord(string[0])+1)+encryption(string[1:])
        
    elif string[0].isupper(): 
        
        return string[0]+encryption(string[1:])
    
    else:
        return encryption(string[1:])
    
userI = input("Enter a message:\n")

print("Encrypted message:\n"+encryption(userI))