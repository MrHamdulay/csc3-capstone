"""Program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character
JP Lanser
3 May"""
#Create a function and use recursion to encrypt a message

def encrypt(string):
    
    
    if len(string) == 0:  #If the string is empty, return an empty string. This is the base case        
            return ''
        
    if not string[0].islower(): #only for lower case as required
            return string[0] + encrypt(string[1:])    
    
    if not string[0].isalpha(): #If the first character is not a letter (eg a space), send the rest of the string (excluding first character to the encrypt function),
        return string[0] + encrypt(string[1:])
    
    else: 
        x= ord(string[0])   #Make a variable and use it to set the the first letter to the next. i.e. a becomes b.
        x+=1
        if string[0] =='z':  #This is to ensure that a 'z' becomes an'a'            
            x -=26
            
        return chr(x) + encrypt(string[1:]) #return the charater associated with x (the variable) and return the rest of the string to the encrypt function
            
    
    
message = input("Enter a message:\n")   #prompt user for input 

print("Encrypted message:")
print(encrypt(message))
    
    
    