"""Assignment 8, question 2
JT
05-05-2014"""

s = input("Enter a message:\n")
count = []


def count_rep(s):
    if len(s) == 1 or len(s) == 0:
        print("Number of pairs:",len(count))
    else:
        if s[0] == s[1]:
            count.append(1)
            return count_rep(s[2:])
        else:
            return count_rep(s[1:])
    
    
count_rep(s)

