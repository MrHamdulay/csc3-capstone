"""counting strings
Lubalethu Dube
7 May 2014"""

messi=input("Enter a message:\n")
def Mr_twinnies(messi):

    if messi.isupper():
        print(messi)
    else:    
        if len(messi) == 0:
            print(messi)
        else:
            if messi[0] == "z":
                print(chr(ord(messi[0])-25), end = "")
                Mr_twinnies(messi[1:])
            elif messi[0] in " ./!,?":
                print(messi[0], end = "")
                Mr_twinnies(messi[1:])
            else:
                print(chr(ord(messi[0])+1), end ="")
                Mr_twinnies(messi[1:])

print("Encrypted message:")
Mr_twinnies(messi)
        