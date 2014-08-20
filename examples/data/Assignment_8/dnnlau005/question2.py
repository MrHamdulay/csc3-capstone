"""count the number of pairs of repeated characters in a string using recursion
Lauren Denny
8 May 2014"""

def count(string):
    if len(string)<=1:                  #if string is 1 character or the empty string, return 0 pairs
        return 0
    else:
        if string[0]==string[1]:        #if first two characters of string are the same, return 1 pair + no. pairs in string from 3rd character onwards 
            return 1 + count(string[2:])
        else:
            return count(string[1:])    #otherwise, return the no. pairs in string from 2nd character onwards

s=input("Enter a message:\n")           #get string
print("Number of pairs:", count(s))     #print no. pairs in string