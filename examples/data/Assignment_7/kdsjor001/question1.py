"""Assignment 7 Question 1
27 April 2014
Jordan Kadish, non-duplicate word list"""

Words=[] #Initialising list
WordsInput=input('Enter strings (end with DONE):\n')
#Add names to list
while WordsInput!='DONE':
    if WordsInput in Words:
        WordsInput=input('')
    else:
        Words.append(WordsInput)
        WordsInput=input('')

print('\nUnique list:')
for word in Words:
    print(word)