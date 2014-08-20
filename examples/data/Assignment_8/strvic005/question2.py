"""program to count the number of pairs of repeated characters in a string
vicky stark
8 may 2014"""


def pairs(words):
    counter=0 #make a counter to count the number of pairs
    if len(words)<=1:
        return counter
    elif words[0]==words[1]:
        counter+=1
        return counter+ pairs(words[2:])
    else:
        return counter+ pairs(words[1:])
       
words=input("Enter a message:\n")
 
counter=pairs(words) #create a second assignment for the words(starting from the word without the second letter)

print("Number of pairs:", counter)

