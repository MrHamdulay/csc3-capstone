'''A program that gets a message from the user and converts all lower cases characters into the next letter
Jacob Ntesang
07 May 2014'''

MSG = input("Enter a message:\n")

def TRY(MSG):
    if MSG == "":
        return ""
    else:
        V = MSG[0]
        if V.islower() and V.isalpha():
            if V == "z":
                V = 'a'
            else:
                V = chr(ord(V)+1)
    return (V + TRY(MSG[1:]))
print("Encrypted message:\n",TRY(MSG),sep="")

                
        
        
    
    
    
