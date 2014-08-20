def num_pairs (n): #Checking for pairs
    if len(n) == 1: #No pairs if one letter
        return 0
    if len(n) == 2 and n[0] == n[1]: #One pair if two letters that are equal
        return 1
    if n[0] == n[1]: #If first two equal, check rest of string
        return 1 + num_pairs(n[2:])
    else: #Else check rest of string excluding first letter
        return num_pairs(n[1:])
    
userString = input("Enter a message:\n") #Printing the result
print ("Number of pairs: " + str(num_pairs(userString)))
    