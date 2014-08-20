#Assignment 8
#Question 2
#Count the number of pairs of repeated characters in a string.  Pairs of characters cannot overlap.

#Get string
string= input("Enter a message:\n")
count=0
def count_pairs(string):
    if len(string)<2: #If the string is shorter than 2 letters
        return 0 #Return 0 because your count is 0
    elif string[0]==string[1]: #If the first two letters are the same
        return 1+count_pairs(string[2:]) #return count and the rest of the string minus the first two letters which are the same
    else:
        return count_pairs(string[1:]) #return the rest of the string minus the first letter
    
print("Number of pairs:",count_pairs(string))
    