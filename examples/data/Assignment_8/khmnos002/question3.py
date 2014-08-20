"""program to encrypt a message using recursion
nosipho khumalo
04 May 2014"""

string = input("Enter a message: \n")
def encrypt(string):
    if string == "":
        return string
    if string[0].isalpha() == False:
        return string[0] + encrypt(string[1:len(string)+1]) 
    elif string[0].islower() == True:
        if len(string) == 1:
            if string[0] == "z":
                return "a"
            else:
                return chr(ord(string[0])+1)
        else:
            if string[0] == " ":
                return " " + encrypt(string[1:len(string)+1])
            elif string[0] == "z":
                return "a" + encrypt(string[1:len(string)+1])        
            else:
                return chr(ord(string[0])+1) + encrypt(string[1:len(string)+1])
    else:
        return string[0] + encrypt(string[1:len(string)+1])

print("Encrypted message: \n", end = "") 
print(encrypt(string))