"""Assignment 8 Question3
Djavan Arrigone 9th May 2014"""

word = ""
def enc (e):
    global word
    if len(e) == 0: #Base case.
        return word
    else: 
        if e[0].islower() == True: #Checks if character is lower case. 
            if e[0] == "z": #If character is z converts to a. 
                o = ord("a") 
            else:
                o = ord(e[0]) 
                o = o + 1 
            word = word + chr(o)
        else: 
            word = word + e[0]
        return enc(e[1:]) #Recursion occurs, sends string from position 2. 

x = input("Enter a message: \n")
print("Encrypted message:")
print(enc(x))
