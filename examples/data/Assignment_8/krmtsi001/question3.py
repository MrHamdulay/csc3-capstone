
s= input("Enter a message: \n")

def encr(s):
    if s=="":        #base case, return the string as it is
        return ""

    
    elif s[0] == "z":             #special condition because after ord(z) its not a
        return "a" + encr(s[1:])    #the recursive step after the above condition is satisfied
   
    
    elif s[0].isupper():
        return s[0] + encr(s[1:])    #when each incriment is uppercase dont do anything to it but return the recursive step
    
    elif not s[0].isalpha():
        return s[0] + encr(s[1:])   #when each incriment does not have the ord posittion 97 to 122 then do not change it but continue with the recursive step
   
    else:
        return  chr(ord(s[0])+1) + encr(s[1:])   #this is when the ord is between 97 and 122 the character gets changed and the recursive step is repeated
message= encr(s)                                         #all the action is made into a variable when the function gets called as the output
      
print("Encrypted message:\n",message, sep="")

        
    
    

   
   
   
   
             
        
    
        
            
            
    
    
