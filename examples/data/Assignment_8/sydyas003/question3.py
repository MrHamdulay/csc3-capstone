#Yaseen Sayed Ismail
#SYDYAS003
#09/05/2014
#Encrypts message

def encrypt(a):
    if(a==""):
        return ""
    else:
        if(a[0].islower() and a[0]!="z"):
            return chr(ord(a[0])+1)+encrypt(a[1::])
        elif(a[0].islower() and a[0]=="z"):
            return "a"+encrypt(a[1::])
        else:
            return a[0]+encrypt(a[1::])
message=input("Enter a message:\n")
print("Encrypted message:",encrypt(message),sep='\n')