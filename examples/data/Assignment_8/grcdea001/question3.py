"""encrypts  a sentance by moving all the letters one more and wrapping around z recursivly
Dean Gracey
4 May 2014"""
def encrypt(sentance):
    newsentance = ""
    if (len(sentance) == 0):
        return newsentance
    
    if sentance[0]=="z":
        newsentance = newsentance + "a"
    elif(ord("a")<=ord(sentance[0])<ord("z")):
        newsentance = newsentance + chr(ord(sentance[0])+1)
    
    else:
        newsentance = newsentance + sentance[0]    
    return newsentance + encrypt(sentance[1:len(sentance)])

    
sentance = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(sentance))