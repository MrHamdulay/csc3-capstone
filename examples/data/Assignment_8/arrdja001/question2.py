"""Assignment 8 Question2
Djavan Arrigone 9th May 2014"""

count = 0
def repchar (c):
    global count
    if len(c) == 0 or len(c) == 1: #Base case.
        return (count)
    else:
        if c[0] == c[1]: #Checks too see if there is repeated character. 
            count = count + 1 # If so, it adds 1 to the global counter. 
            return repchar(c[2:]) #Recursion occurs sending string from after repeated characters. 
        else:
            return repchar(c[1:])
    
x = input("Enter a message: \n")
print("Number of pairs:" , repchar(x))
