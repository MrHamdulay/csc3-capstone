"""Assignment 7, Question 1
Tejasvin Bagirathi BGRTEJ001
program to produce unique list of strings"""

#user inputs string list
words = []
print('Enter strings (end with DONE):')
wrd_input = input()

#Sentinal loop for user input of strings
while wrd_input != 'DONE':
    #Add words to list
    words.append(wrd_input)
    wrd_input = input()

#Decalre new list
new_wrds = []

#Loop to check if word is in new word list and append if not present
for i in words:
    #if the word is in the list, continue
    if i in new_wrds:
        continue
    #Or else add the word to the list
    else: new_wrds.append(i)

#Print out unique list
print()
print('Unique list:')
for i in new_wrds:
    print(i)