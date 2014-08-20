x= input("Enter a message:\n")
y=0

def encryption(x,y):
    if y >= len(x):
        return("")
    
    
    elif y < len(x):
        if x[y].islower()==True:
            
            
            if x[y]== "z":
                return "a" + encryption(x,y+1)
            else:
                return chr(ord(x[y])+1) + encryption(x,y+1)
            
            
        else:
            return x[y] + encryption(x,y+1)
        
print("Encrypted message:")
print(encryption(x,y))