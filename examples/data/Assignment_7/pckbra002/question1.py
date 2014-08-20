"""program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates"""
"""Brandon Pickup"""
"""Assignment 7 Question 1"""
"""27 April 2014"""
words = []
word = input("Enter strings (end with DONE):\n")
while word != "DONE":
    words.append(word)
    word = input("")
print("\nUnique list:")
usedWords = [] #array to store used words to check against for duplicates
i=0
while i < len(words):
    if words[i] in usedWords:#if the word is a duplicate, only increase the counter
        i+=1
    else:#if the word is not a duplicate, print it and then add it to the list of already used words
        print(words[i],"")
        usedWords.append(words[i])