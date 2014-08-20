"""Encrypt a sentense by moving lowercase letters to the next letter
Kiara Ramjith
May 2014"""

def encr(s,e):
    if(len(s)!=0): #if the string has characters; come in
        if(s[0]=="z"): #if the current letter that we want to work with is z, make it a 
            e=e+"a"
            return encr(s[1:],e)
        elif(97<=ord(s[0])<122): # using ascii table, if it lower case letters
            e=e+chr(ord(s[0])+1) # add the next letter to the encrypted string
            return encr(s[1:],e)
        else:
            e=e+s[0] #if it is not a lower case letter, just add the current letter
            return encr(s[1:],e)
    else:
        return e
    
if __name__== "__main__":
    s=input("Enter a message:\n")
    em=encr(s,"")
    print("Encrypted message:\n"+em)
            
    