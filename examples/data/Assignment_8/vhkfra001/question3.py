'''Program that uses recursion to encrypt a message
Frans van Hoek
8 May 2014'''

def encrypt(s, i):
    new = ""
    if i == len(s)-1:
        if s[i].isalpha() == True and s[i].lower() == s[i]:
            if s[i] == 'z':
                new += 'a'
                return new
        
            else:
                new += chr(ord(s[i])+1)
                return new
        else:
            new += s[i]
            return new
            
    
    else:
        if s[i] == 'z':
            new = "a" + encrypt(s, i+1)
            return new
            
            
        elif s[i].isalpha() == True and s[i].lower() == s[i]:
            new = chr(ord(s[i])+1) + encrypt(s, i+1)
            return new
        
        else:
            new = s[i] + encrypt(s, i+1)
            return new
        
message = input("Enter a message:\n")
new_message = encrypt(message, 0)
print ("Encrypted message:\n" + new_message)
