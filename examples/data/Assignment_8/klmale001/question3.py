"""program to encrypt lower case strings
Alexi Kalamoudacos
8 May 2014"""

#ask user for message
x = input("Enter a message:\n")
i = 0
#making a list for the encrypted letters
new_x = []

def encrypt(x):
    global i
    global new_x
    new_char = ""

    if i < len(x):  #make recursion end when last character is analysed
        uni_chr = ord(x[i])
        
        #only encrypt uppercase letters
        if uni_chr < 97 or uni_chr > 122:
            new_x.append(chr(uni_chr))
            i+=1
            return encrypt(x)
        
        #Encrypt lower case characters except z 
        elif uni_chr in range(97,122):
            new_chr = chr(uni_chr + 1)
            new_x.append(new_chr)
            i+=1
            return encrypt(x)
        
        #encrypting z
        elif uni_chr == 122:
            new_x.append("a") #Hard coding
            i+=1
            return encrypt(x)
    
    else: #Print 
        new_x = "".join(new_x)
        print("Encrypted message:\n", new_x, sep="")
        
if __name__=="__main__":
    encrypt(x)