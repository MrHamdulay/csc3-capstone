''' Assignment 8, question 2
Use recursion to count number of pairs of repeated characters in a string
Tristan Subroyen
4 May 2014 '''

# These lists will hold characters:
char1 = [] # Holds all unique characters in given string
char2 = [] # Holds all unique repeated characters in given string

def countPairs (string):
    ''' This function is recursive - it counts number of paired characters in a string using lists and recursion '''
    # base case:
    if string == '':
        return 0
    else:
        # if the string is still in required index
        if len(string) > 1:
            if string[0] == string[1]: # if two pairs are the same...
                char1.append(string[0]) # add it to the list
                return countPairs (string[2:]) # then use recursion in the rest of the string (skipping the one character because it is a pair)
            else:
                return countPairs (string[1:])

# Ask user: input and display result
message = input("Enter a message:\n")
countPairs (message)
print("Number of pairs:",len(char1))