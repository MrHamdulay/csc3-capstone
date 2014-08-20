"""ASSIGNMENT 8 QUESTION 3- ENCRYPT A MESSAGE (SHIFT ONE LETTER OVER)
EMMA JORDI
8 MAY 2014"""
#HAD TO REMOVE "O" FROM VAIRIABLES. 

riginal=input("Enter a message:\n")
#define function
def encrypt(riginal):
    
    #base case
    if riginal == "" or riginal.isupper():
        return riginal
    else:
        sliced = riginal[0]
        rder = ord(sliced)
        if sliced == " " or sliced == ".":
            encrypted = sliced
            
        elif rder>=122: #for z
            encrypted= rder-25
            encrypted= chr(encrypted)
            
        else:
            encrypted= rder+1
            encrypted = chr(encrypted)
        
        return encrypted + encrypt(riginal[1:len(riginal)])
    
print("Encrypted message:\n",encrypt(riginal), sep="")

