#Khyati Jinerdeb
#Assignment 8
#Date Submitted:09/05/2014
#program to encrypt a message


def encrypt(string,x):
    if len(string)==0:
        return print("Encrypted message:\n"+x) # the encrypted message is returned if the the length of the string is 0
    else:
        if 97<=ord(string[0])<122:   #to check if the letter in the string is found between a to z
            z=ord(string[0])
            x=x+chr(z+1)             #using the chr function to to convert numeric to character
            encrypt(string[1:],x)    #using slicing from first character to the previous last
        else:
            x+=string[0]
            encrypt(string[1:],x)
            
anything=input("Enter a message:\n")
encrypt(anything,"")

            
            
            
            
        
    

        
        
