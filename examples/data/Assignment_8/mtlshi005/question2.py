mes=input("Enter a message:\n")

def countrep(mes):
    if len(mes)<2:                  # if there is only one letter left, no pair possible
        return 0        
    elif mes[0]==mes[1]:                   #check if letter is equal to consecutive letter, then return 
        return 1 + countrep(mes[2:])  
    else: 
        return countrep(mes[1:])

print("Number of pairs:",countrep(mes))