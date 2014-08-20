# Mathew Finlayson - FNLMAT001
# Assignment 8 - Question 2
# 04/05/2014

def numRepeatedChars (s):
    """recursive function that counts the number of pairs of repeated characters in a string (no overlap)"""
    if len(s) < 2: # end case
        return 0
    if s[0] == s[1]: # if the first character same as the 2nd character
        return numRepeatedChars(s[2:]) + 1 # shorten string by 2 and recall numRepeatedChars
    else: 
        return numRepeatedChars(s[1:]) # shorten string by 1 and recall numRepeatedChars

# gets input from user, calculates number of pairs and prints out 
print("Number of pairs:", numRepeatedChars(input("Enter a message:\n"))) 