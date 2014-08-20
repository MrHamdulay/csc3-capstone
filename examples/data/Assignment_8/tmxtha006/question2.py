"""This program count the number of pairs of repeated charaters in a string
Hebert Tema
TMXTHA006
04 May 2014"""


def count(string):
    """count the number of pairs of repeated charaters in a string"""
    if len(string)<=1: return 0
    elif string[0]==string[1]:
        return 1+count(string[2:])
    else:
        return count(string[1:])

#get the input from the user
string=input("Enter a message:\n")

#call the count function
answer=count(string)

#output the results
print("Number of pairs:",answer)