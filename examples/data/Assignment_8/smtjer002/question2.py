"""A program that counts the number of repeated characters in a string using a recursive function
by Jeremy Smith SMTJER002
4 May 2014"""

def count_pairs(string):
    """counts the number of paired letters in a string"""
    #stopping point is if the length of the string is only 1 or 0 characters left
    if len(string) <= 1:
        return 0
    #returns 1 if two adjacent characters are the same, else returns 0, and recursively processes the rest of the string
    elif string[0] != string[1]:
        return 0 + count_pairs(string[1:])
    elif string [0] == string[1]:
        return 1 + count_pairs(string[2:])
    
string = input("Enter a message:\n")
count = count_pairs (string)
print("Number of pairs:",count)    