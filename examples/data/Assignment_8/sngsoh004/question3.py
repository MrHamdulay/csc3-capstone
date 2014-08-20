#Soham Hanuman Singh
#SNGSOH004
#Assignment 8
#Question 3

def encryption(string):
    if string[0]==" ":
        return " "+encryption(string[1:]) #if there is a space
    
    elif (string[0]==string[len(string)-1]): #If it is the last character
        
        if string[0].islower(): #only encrypt if its a lower case character
            if string[0]=="z": #changing z's to a's
                return "a"
            else:
                return chr(ord(string[0])+1)
        else:
            return string[0]
        
    elif string[0].islower(): #encrypting when it is not the last character
        
        if string[0]=="z":
            return "a"+encryption(string[1:])
        
        else:
            return chr(ord(string[0])+1)+encryption(string[1:])
        
    elif string[0].isupper(): #do not encrypt the character if it is upper case
        return string[0]+encryption(string[1:])
    
    else:
        return encryption(string[1:])
    
message = input("Enter a message:\n")
print("Encrypted message:\n"+encryption(message))