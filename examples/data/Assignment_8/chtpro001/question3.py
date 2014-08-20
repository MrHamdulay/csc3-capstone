b = input('Enter a message:\n')

def conve(b):
    if b == "":
        return ""
    if b == b.upper:   
        print("Encrypted message: ")
        return b
    elif b[0] == "z":
        return "a" + conve(b[1:])       
    elif b[0].isupper():
        return b[0] + conve(b[1:])      
    elif b[0] == " ":
        return " " + conve(b[1:])        
    elif b[0] == ".":
        return "." + conve(b[1:])  
    else:
        return chr(ord(b[0])+1) + conve(b[1:])   
print("Encrypted message: ")    
print(conve(b))

        