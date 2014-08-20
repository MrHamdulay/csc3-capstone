"""program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character
Thiloshni Moodley
7 May 2014"""

#user asked to enter a message
message = input("Enter a message:\n")
x = 0
message_list = [] # Create empty list to store encrypted

def encrypt(message):
    global message_list
    global x
    new_character = ""

    if x < len(message):  
        uni_character = ord(message[x]) #convert character to unicode
        
        if uni_character < 97 or uni_character > 122: #only encrypt if lower- case(lower case unicode = 97-122)
            message_list.append(chr(uni_character))
            x= x + 1
            return encrypt(message)
         
        elif uni_character in range(97,122): #Encrpyt range a to y
            new_character = chr(uni_character + 1)
            message_list.append(new_character)
            x= x + 1
            return encrypt(message)
        
        elif uni_character == 122: #when character is z, exception
            message_list.append("a") 
            x = x + 1
            return encrypt(message)
    
    else: 
        message_list = "".join(message_list) #joins all encrypted
        print("Encrypted message:\n", message_list, sep="")
        
if __name__=="__main__":
    encrypt(message)