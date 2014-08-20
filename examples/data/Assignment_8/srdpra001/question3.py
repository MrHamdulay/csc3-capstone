"""
Prashanth Sridharan
SRDPRA001
Assignment 08
Question 03
"""
#i is the variable name for the sentence
def Encryptf(i): #function Encryptf defined as the function to encrypt the sentence with the variable name i
    
    if i[0]==" ": #terminator step of the recursive step
        return " "+Encryptf(i[1:])     
    elif (i[0]==i[len(i)-1]): #The recursive step
        if i[0].islower():  #checks if input to lower case          
            if i[0]=="z": #returns a if z is reached.
                return "a"
            else:                
                return chr(ord(i[0])+1)
        else:
            return i[0]
#the recursive steps
    elif i[0].isupper(): 
        return i[0]+Encryptf(i[1:])    
    elif i[0].islower(): 
        if i[0]=="z":
            return "a"+Encryptf(i[1:])
        else:
            return chr(ord(i[0])+1)+Encryptf(i[1:])
    else:
        return Encryptf(i[1:])
user_input = input("Enter a message:\n")
print("Encrypted message:\n"+Encryptf(user_input))