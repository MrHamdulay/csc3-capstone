'''Wade Cresswell
Question 3'''
string = input("Enter a message:\n")
def encodestring(x):
    if x[0].islower(): #if the letter is lower case
        if len(x) == 1:
            if x[0]=="z":
                return "a"
            else:
                return chr(ord(x[0])+1)
        elif x[0]=="z":
            return "a" + encodestring(x[1:]) #if its z, wrap around to other side of alphabet
        else:
            return chr(ord(x[0])+1) + encodestring(x[1:]) #returns the encoded character and the rest of the string
    else: #if not, go on as usual
        if len(x) == 1:
            return x[0]
        else: 
            return x[0] + encodestring(x[1:])
print("Encrypted message:")
print(encodestring(string)) #print encoded string
