__author__ = 'JNSJOH014'
"""Count the number of pairs of repeated characters in a string"""
def count_pairs(s):
    if len(s)<2:
        return 0
    elif s[0]==s[1]:
        return 1+count_pairs(s[2:])
    else:
        return count_pairs(s[2:])

s = input("Enter a message:\n")
print("Number of pairs:",count_pairs(s))