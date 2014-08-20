#program to count the number of pairs in a string
#kiyarah pillay
#10 may 2014

#get input from user
message=input("Enter a message:\n")
def pairs(message):
#base case
    if (len(message)) <2 :
        return 0
#if the first letter is the same as the second
    elif (message[0]) == (message[1]):
        return 1 + pairs(message[2:])

    else:
        return pairs(message[1:])
#call the function to get the number of pairs
print ("Number of pairs:" ,(pairs(message)))

    


