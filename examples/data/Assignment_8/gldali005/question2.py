#program that uses a recursive function to count the number of pairs of repeated characters in a string.
#Ali Goldstein
#8 May 2014

#function to find out the number of pairs of repeated characters in the string
def char_pairs(i):
    if len(i) == 1 or len(i) == 0:
        return 0    

    if i[0]==i[1]:
        return 1+char_pairs(i[2:])
        
    else:
        return 0+char_pairs(i[1:])        


#prompt user to enter in a message and call the function to count the number of pairs of repeated characters in the message
message=input("Enter a message: \n")
print("Number of pairs:", char_pairs(message))
