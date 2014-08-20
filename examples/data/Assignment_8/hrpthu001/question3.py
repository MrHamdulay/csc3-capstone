"""Program to encrypt a message
thushar hariparsad
7 May 2014"""


message = input("Enter a message:\n")
counter = 0
new_msg = [] #list for encrypted message

def encrypt(message):
    global counter
    global new_msg
    new_char = ""

    if counter < len(message): 
        #Convert character into unicode value
        uni_chr = ord(message[counter])
        
        #If character is upper case do not encrypt
        if uni_chr < 97 or uni_chr > 122:
            new_msg.append(chr(uni_chr))
            counter+=1
            return encrypt(message)
        
        #Encrypt all lower case letters from a to y 
        elif uni_chr in range(97,122):
            new_chr = chr(uni_chr + 1)
            new_msg.append(new_chr)
            counter+=1
            return encrypt(message)
        
        #If character is "z" encrypt to "a" 
        elif uni_chr == 122:
            new_msg.append("a") 
            counter+=1
            return encrypt(message)
    
    else: #Print encrypted message
        new_msg = "".join(new_msg)
        print("Encrypted message:\n", new_msg, sep="")
        
if __name__=="__main__":
    encrypt(message)