"""Keyoolin Padayachee
Right aligning program
24 April 2013"""

def align():
    print("Enter strings (end with DONE):") 
    string = [] #creates an array
    loop = ""
    length = 0 
    while loop != "DONE":
        loop = input()
        if loop == "DONE": #loop breaks if input was DONE
            break
        string.append(loop) # adds the input to the array
        if len(loop)>length: # checks if the length of the input was bigger than the largest string
            length = len(loop)
    print()
    print("Right-aligned list:")
    for i in range(len(string)):
        print("{0:>{1}}".format(string[i],length)) # prints and formats the inputted values

align()