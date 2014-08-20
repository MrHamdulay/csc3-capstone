#A program where the user can enter a list of strings, whereafter the strings are printed in the same order but without duplicates
#Author: Emiel Zyde
#Date: 27 April 2014

#prompt the user for a first input and initialize an empty list
word = input("Enter strings (end with DONE):\n")
words = []

#check that the input is not the sentinel and then continue to reprompt until the sentinel is entered
#we must also append each value to the list
while word != "DONE":
    words.append(word)
    word = input("")

#make a list of the unique words in the sentence 
#initiliaze an empty list, check if the word is in the list and add it in if it isn't 
unique_words = []
for word in words:
    if word in unique_words:
        continue
    else:
        unique_words.append(word)
        
#print out the list of words in the same order, but without duplicates
print("\nUnique list:")
for word in unique_words:
    print(word)