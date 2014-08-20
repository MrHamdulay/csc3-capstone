#Azhar Aboobaker
#ABBAZH001
#07/05/2014

message = input("Enter a message:\n")

def emessage(x):
    if x == "":
        return ""
    elif x[0].islower():
        if x[0] == 'z':
            return 'a' + emessage(x[1:])
        else:    
            y = ord(x[0]) + 1
            return chr(y)+emessage(x[1:])
    else:
        return x[0]+emessage(x[1:])
    
print("Encrypted message:\n"+emessage(message))
        
        
        