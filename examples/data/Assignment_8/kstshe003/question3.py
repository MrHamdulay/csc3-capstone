#sheldon kisten
#8 may 2014
#encrypt message

def encrypt(string,y):
    if len(string)==0:
        return print("Encrypted message:\n"+y) 
    else:
        if 97<=ord(string[0])<= 122:
            z=ord(string[0]) - 97
            y=y+chr((z+1) % 26 + 97)
            encrypt(string[1:],y)
        else:
            y+=string[0]
            encrypt(string[1:],y)
            
anything=input("Enter a message:\n")
encrypt(anything,"")

            
            
            
            
        
    

        
        
