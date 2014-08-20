# anna borysova
# q2, ass8
# 2014 - 05 - 08

def encr(string, i=0):   
    if i == len(string)-1:
        if string[i].islower():
            if string[i] == "z":
                return "a"
            return chr(ord(string[i])+1)
        else:
            return string[i]
    if not string[i].islower():
        return string[i] + encr(string, i+1)
    if string[i] == "z":
        return "a" + encr(string, i+1)
    return  chr(ord(string[i])+1) + encr(string, i+1)
 
message = input("Enter a message:\n")
print("Encrypted message:\n", encr(message), sep="")