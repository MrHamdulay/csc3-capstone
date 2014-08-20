"""question2.py :- count the number of pairs of repeated characters
Author : Musa Xakaza
Date : 06/05/2014"""

def countPairs(s):
    if len(s) < 2:
        #if there's one character or none return zero
        return 0
    elif s[0] == s[1]:
        #if there's pair, count it and start from third character in a string
        return 1 + countPairs(s[2:])
    else:
        #if a pair isn't yet found, remove the first character in a string
        return countPairs(s[1:])

#get message
msg = input("Enter a message:\n")
print("Number of pairs: ",countPairs(msg),sep='')