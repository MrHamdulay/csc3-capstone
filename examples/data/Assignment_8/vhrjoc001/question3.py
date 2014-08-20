#vhrjoc001
#question 3 assignment 8
#encrypting a message by converting all lowercase characters to the next character (with z transformed to a).

def encrypt(messege):
    if messege=="":
        return messege
    elif (ord(messege[0]))>=ord("a") and ord(messege[0])<=ord("z"):
        pcassignment=ord(messege[0])
        pcassignment+=1
        if pcassignment>ord("z"):
            pcassignment-=26
        return chr(pcassignment)+ encrypt(messege[1:])
    else:
        return messege[0] + encrypt(messege[1:])
secretmessege=input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(secretmessege))

    
    
