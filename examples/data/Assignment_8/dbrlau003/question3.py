#Lauren de Bruyn: DBRLAU003
#Recursive function to encrypt a message by converting all lowercase characters to the next character
#7 May 2014

strings=[]

def encrypt(string):
    
    global strings
    new_chr = " "
    
    if  len(string)>0:
        orig_chr = ord(string[0])
        
        if (orig_chr) < 97 or orig_chr > 122:
            strings.append(chr(orig_chr))
            
            return encrypt(string[1:])
            
        elif (orig_chr) == 122:
            strings.append('a')
            
            return encrypt(string[1:])
       
        elif (orig_chr) in range(97,122):
            new_chr = chr(orig_chr + 1)
            strings.append(new_chr)
            
            return encrypt(string[1:])
    
    else:
        strings = "".join(strings)
        print("Encrypted message: \n", strings, sep="")
        
if __name__ == "__main__":
    string = input("Enter a message: \n")
    encrypt(string)