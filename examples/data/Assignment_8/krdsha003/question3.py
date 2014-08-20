"""Assignment8 question 3
encrypt a message by converting all lowercase characters to the next character
Shaheen Karodia
KRDSHA003
2014-05-04"""

def encrypt(string):
    """converts all lowercase characters in a string to next character in alphabet"""
    
    
    #base case to ensure function stops recursing 
    if len(string)==1:
        
        if string== " ": #does not shift spaces down the unicode code
            return " "
        elif string=="z":   #ensures z wraps back and is converted to 'a'
            return "a"
        elif string.isalpha()==False:
            return string          
        elif string.islower()==False:
            return string
        
        else:
            return chr(ord(string[0])+1)   #shifts each character one down the alphabet 
        
    else:
        #return the shifted character and calls the function to recurse through a smaller string 
        
        if string[0]=="z":
            return "a"+ encrypt(string[1:])    
        
        elif string[0]== " ":
            return " "+ encrypt(string[1:])
        elif (string[0]).isalpha()==False:
            return string[0] + encrypt(string[1:])
        elif (string[0]).islower()==False:
                    return string[0] + encrypt(string[1:])
        
        else:
            return chr(ord(string[0])+1) + encrypt(string[1:])
  
  


       
def main():
    
    x=input("Enter a message:\n")
    print("Encrypted message:")
    print(encrypt(x))
    
main()
    
    
    

    