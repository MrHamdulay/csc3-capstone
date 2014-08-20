# counting number of pairs
# Budeli Rendani
# BDLREN001
# 07/05/2014

def count(string): # creating a function to count the words
    if len(string)==1: # if lenght of string is 1 return 0 since no pairs are present(The base case)
        return 0
    
    elif string=="": # If string is an empty string return 0 since no string is present(The base case)
        return 0
    # The function then counts the number of pairs in the string
    elif string[0] == string[1]: 
            return 1 + count(string[2:])    
    
    else:
        return 0 + count(string[1:])

string=input("Enter a message:\n") # Entering the string ny the user
number=count(string)  #assigning function to a variable

print("Number of pairs:",number)

