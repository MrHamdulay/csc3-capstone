"""Question 3: encrypts a message you type in
Galya Wolov
9 May 2014"""

message= input("Enter a message:\n") # asks 4 a message

def encrypt(x):

                            
    if x[0].islower(): #follows instructions only changes lower case
        
               
        if len(x)==1:
            if x[0]=="z":
                return "a" #follows 26 letter follow on
            else:
                return chr((ord(x[0])+1)) # uses unicode to encode only one letter therefore no recursion
        
        
        elif x[0]=="z":
                return "a" + encrypt(x[1:])  #+ recursive step but otherwise as above      
               
        else:
            return chr((ord(x[0])+1))+ encrypt(x[1:]) #if not z then just recursive step using unicode
    
    else:
        
        if len(x) ==1:
            return x[0] #this is because not lowercase
                  
        else:
            return x[0] + encrypt(x[1:])      
        

print("Encrypted message:\n",encrypt(message),sep='') #print statment which introduces encrpyted message
