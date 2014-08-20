"""Assignment 8, Question 2
Tejasvin Bagirathi BGRTEJ001
program to count number of simolraneous """

#Prompt user input
string = input('Enter a message:\n')
pairs = 0

def num_pairs(word):
    global pairs
    #If string length equals 1, print pair count
    if len(word) <= 1:
        print("Number of pairs:", pairs)
    #If the first and second letter in the string are the same add one to pair count
    elif word[0] == word[1]:
        pairs += 1
        #Delete first two letters from string
        word = word[2:]
        return num_pairs(word)
    #Else if first two aren't the same, delete the first letter and recurse
    else:
        word = word[1:]
        return num_pairs(word)
    
num_pairs(string)