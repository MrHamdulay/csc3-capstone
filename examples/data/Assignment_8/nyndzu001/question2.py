string=input("Enter a message:\n")

def pairs(string):
    counter=0
    if len(string)<2:
        return counter
    elif string[0]==string[1]:
        counter+=1
        return counter + pairs(string[2:])
    
    else:
        return counter + pairs(string[1:])
    
print("Number of pairs:", pairs(string))