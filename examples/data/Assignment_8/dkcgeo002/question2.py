__author__ = 'George de Kock'
"""program that uses a recursive function to count the number of pairs of repeated characters in a string
2014-05-05"""


repeated = []


def countpairs(text):
    if len(text) > 1:
        if (text[0] == text[1]): #and (text[1] not in repeated)
            repeated.append(text[0])
            text = text[1:]
        countpairs(text[1:])


word = input("Enter a message:\n")
countpairs(word)
print("Number of pairs:",len(repeated))