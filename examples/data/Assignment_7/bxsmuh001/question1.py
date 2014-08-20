#Assignment 7, Question 1
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Created: 27/04/2014

#This program is designed to output a list of words
#Pre-condition: Input list of words followed by sentinel "DONE".
#Post-condition: Output  number of words in same order without repeating words.
wordsList = []
usedList = []

word = ""
print("Enter strings (end with DONE):")
while (word != "DONE"):
    word = input()
    if(word == "DONE"):
        break
    wordsList.append(word)

print("\nUnique list:")
#Looping through list.
for i in range(len(wordsList)):    
    if(wordsList[i] in usedList):
        continue #Skip a word if it already exists.
    print(wordsList[i])
    usedList.append(wordsList[i]) #If a word is used, insert it in a used list. This will allow to check for duplication in case the same word appears again.
