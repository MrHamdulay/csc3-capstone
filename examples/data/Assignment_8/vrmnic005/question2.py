#VRMNIC005
#Assignment 7, question 2

def pairs(string):
    if len(string) < 2:
        return 0
    elif string[0] == string[1]:
        return 1 + pairs(string[2:])
    else:
        return pairs(string[1:])

string = input("Enter a message: \n")
    
print("Number of pairs:", pairs(string))

