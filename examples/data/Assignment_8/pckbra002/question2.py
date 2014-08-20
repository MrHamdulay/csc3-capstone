"""Brandon Pickup"""
"""3 May 2014"""
"""Assignment 8 Question 2"""
sent = input("Enter a message:\n")
def count_pairs(s):
    """ function to count the number of pairs of repeated characters in a string"""
    if len(s)<2:
        return 0
    elif s[0] == s[1]:#if 2 consecutive letters are the same, return 1 + the string from after the pair of letters
        return 1 + count_pairs(s[2::])
    else:#not the same, just check the string from the next position to the end
        return count_pairs(s[1::])
print("Number of pairs:", count_pairs(sent))