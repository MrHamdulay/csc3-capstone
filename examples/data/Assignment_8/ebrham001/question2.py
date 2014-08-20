'''Recursive function counting number of pairs in a string
HAMZA EBRAHIM
09/05/2014'''

# Assignment 8 - Question 2

# recursive function that counts the number of pairs of the same character in a string

def pairs(s):
    if len(s) == 1:
        return 0
    if len(s) == 2 and s[0] == s[1]:
        return 1
    elif s[0] != s[1]:
        return pairs(s[1:])
    else:
        return 1 + pairs(s[2:])

# main function which prompts user for a string, then invokes pairs function above to count the number of pairs in the string
    
def main():
    s = input("Enter a message:\n")
    pairs(s)
    print("Number of pairs:", pairs(s))
    
main()    

# program ends        