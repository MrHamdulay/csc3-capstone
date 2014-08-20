"""QUESTION 1, Assignment 7
Charlie Shang
SHNHUA002"""

string = ''
print('Enter strings (end with DONE):')
wordlist = []
while not string.upper() =='DONE':# repeat input while the user is not done.
    string = input()
    if string not in wordlist: #f the input isnt already in the list, then append
        wordlist.append(string)
        
del wordlist[-1] #deletes last item (DONE)

print('\nUnique list:')

for k in range(len(wordlist)):#prints items in the list on a new line
    print(wordlist[k])
    