def encrypt(string):
    
    if len(string) == 0:
        return ""
    elif string[0].isupper():
        return string
    elif string[0] == " ":
        return " " + encrypt(string[1:])
    
    elif string[0] == "z":
        return "a" + encrypt(string[1:])
    elif string[0] == ".":
        return "." + encrypt(string[1:])

    else:
        x = string[0]
        y =ord(x) - 97
        z= chr(y+1 +97)
        return z + encrypt(string[1:])
          
    
    
print("Encrypted message:\n",encrypt(string = input("Enter a message:\n")), sep ="")