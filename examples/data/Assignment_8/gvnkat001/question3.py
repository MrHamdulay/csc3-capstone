"""Write a program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a). You MUST NOT use any form of loop in your program!"""
"""6th May 2014 Katlego Gaveni"""

codeword="" #create empty string

def encode(s):
    
    global codeword#global variable
    if s=="":
        return ""
    else:
        
        if len(s)==1:#stopping condition once the string has a length of 1
            if s[0]=="z":#if the letter in the string is z the function returns "a"
                codeword+="a" 
                return codeword #return our new encrypted word
            elif s[0]== " ":
                codeword+=" "
                return codeword
            elif s[0]==".":
                codeword+="."
                return codeword
            else:
                num=ord(s[0])+1#shift the order of unicode number for each letter by 1
                codeword += chr(num)#add the new character to codeword
                return codeword
            
            
        elif s[0]==" ":
            codeword+=" "
            return encode(s[1:])        
            
        elif s[0]=="z":
            codeword += "a" 
            return encode(s[1:])
        elif s[0]==".":
            codeword+="."
            return encode(s[1:])
        else:
            num=ord(s[0])+1
            codeword += chr(num) 
            return encode(s[1:])
        
if __name__=="__main__":
    s=input("Enter a message:\n")#input from user
    
    if s == s.lower():
        encode(s)
        print("Encrypted message:\n",codeword,sep="")
    else:
        print("Encrypted message:\n",s,sep="")