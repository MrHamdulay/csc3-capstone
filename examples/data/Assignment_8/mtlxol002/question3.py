"""CSC1015F Assignment 8 Question 3
Xola Matlanyane MTLXOL002
9 May 2014"""

#define an encrypting function
def enc(s,i):             #for all strings (s) and integers (i)
    newenc=""             #creating a variable for new encryption
    if i == len(s)-1:       #i is the place-holder for each character (function checks for the end of the string)
        
        if s[i] == "z":          #accounting for lower case z's (making a "z" an "a")
            newenc= "a"
            return newenc
        elif s[i].isalpha() == True and s[i].lower() == s[i]:        #check the alphabetical nature and adding to string
            newenc= chr(ord(s[i])+1)
            return newenc
        else:
            newenc= s[i]     #ignoring those characters that are not alphabetical
            return newenc
        
    else:
        if s[i] == "z":          #accounting for lower case z's (making a "z" an "a")
            newenc= "a" + enc(s,i+1)
            return newenc
        elif s[i].isalpha() == True and s[i].lower() == s[i]:      #check the alphabetical nature and adding to string
            newenc= chr(ord(s[i])+1) + enc(s,i+1)
            return newenc
        else:
            newenc= s[i] + enc(s,i+1)     #ignoring those characters that are not alphabetical
            return newenc
       
message= input("Enter a message:\n")
print("Encrypted message:")
print (enc(message,0))
