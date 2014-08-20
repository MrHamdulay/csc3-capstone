# Assignment 8 (Q2)
# A program that counts the number of pairs of repeated characters in a string (pairs of characters cannot overlap)
# Written by: Laene van Niekerk
# VNKLAE001

def count(s):
    if len(s) < 2:      # If there are less than 2 letters there cannot be a pair
        return 0
    elif s[0] == s[1]:
        return 1 + count(s[2:])     # If the characters are equal, add to counter and move on
    elif len(s) > 2:
        if s[1] == s[2]:        # Second possible combination of pairs
            return 1 + count(s[2:])
        else:
            return count(s[2:])
    else:
        return count(s[2:])     # Else move on
    
x = input("Enter a message:\n")
print("Number of pairs:", count(x))