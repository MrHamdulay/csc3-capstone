def Encrypted_message(string):
    if len(string)==1:
        if string=="z":
            return "a"
        return chr(ord(string)+1)
    if string[0]==" ":
        return " "+Encrypted_message(string[1:])
    if string[0]==".":
        return "."+Encrypted_message(string[1:])
    if string.isupper():
        return string
    else:
        if string[0]=="z":
            return "a"+Encrypted_message(string[1:])
    if ((string[0] != ".")and(string[0] != " ")):
        return chr(ord(string[0])+1) +Encrypted_message(string[1:])
b=input("Enter a message:\n")
print("Encrypted message:")
encrypt = Encrypted_message(b)
if (encrypt[-1] == "/"):
    encrypt = encrypt[0:len(encrypt)-1] + "."

    
print(encrypt)


     