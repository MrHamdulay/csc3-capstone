


def enc(s,i):             
    newenc=""             
    if i == len(s)-1:       
        
        if s[i] == "z":          
            newenc= "a"
            return newenc
        elif s[i].isalpha() == True and s[i].lower() == s[i]:       
            newenc= chr(ord(s[i])+1)
            return newenc
        else:
            newenc= s[i]    
            return newenc
        
    else:
        if s[i] == "z":         
            newenc= "a" + enc(s,i+1)
            return newenc
        elif s[i].isalpha() == True and s[i].lower() == s[i]:      
            newenc= chr(ord(s[i])+1) + enc(s,i+1)
            return newenc
        else:
            newenc= s[i] + enc(s,i+1)    
            return newenc
       
message= input("Enter a message:\n")
print("Encrypted message:")
print (enc(message,0))
