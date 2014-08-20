#question3

def encrypt(word,ii):
    length=len(word)-1
    if ii==length+1:
        return ""
    else:
        if not word[ii]==" ":
            if word[ii].islower():
                if word[ii]=="z":
                    return "a" + str(encrypt(word,ii+1))
                else:
                    return chr(ord(word[ii])+1) + str(encrypt(word,ii+1))
            else:
                return word[ii] + str(encrypt(word,ii+1))
        else:
            return " " + str(encrypt(word,ii+1))
        
msg=input("Enter a message:\n")

print("Encrypted message:")
print(encrypt(msg,0))

