"""question 1 assignment 7
Adam Rosendorff
02 May 2014"""
#program to return list of unique words only
strings = []
print('Enter strings (end with DONE):')
readstring = input()
while (readstring != 'DONE'):
    if not readstring in strings: #check if the word is already saved
        strings.append(readstring)
    readstring = input()
if len(strings) != 0:
    length = len(max(strings, key=len))
print('\nUnique list:')
for i in range(len(strings)):
    print(strings[i])
