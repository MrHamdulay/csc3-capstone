"""Aiden Walton
WLTAID001
Question 2 - Assignment 8"""
def pairs(s):
    if len(s)<=1:
        return 0
    elif s[0]==s[1]:
        return 1 + pairs(s[2:])
    else:
        return pairs(s[1:])
    

s=input("Enter a message:\n")
print("Number of pairs:",pairs(s))