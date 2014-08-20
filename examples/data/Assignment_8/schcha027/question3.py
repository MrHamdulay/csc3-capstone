# 09/05/2014 
# SCHCH027
# Question1
message=input("Enter a message:\n")
count=0
encrypted=""
# Encrypts a message
def encrypt_mess(message,count,encrypted):
    length=len(message)
	#checks the corresponding ASCII Value of each character
    if count<length:
        if 97<=ord(message[count])<=121:
            encrypted=encrypted+chr(ord(message[count])+1)
            count+=1
            encrypt_mess(message,count,encrypted)
            #if character is z, shifts character to 
        elif (ord(message[count])==122):
            encrypted=encrypted+"a" 
            count+=1
            encrypt_mess(message,count,encrypted)
            
        else:
		#else appends all non lower case letters as normal
            encrypted=encrypted+message[count]
            count+=1
            encrypt_mess(message,count,encrypted)
    else:
        
        print("Encrypted message:")
        print(encrypted)
    
    
encrypt_mess(message,count,encrypted)