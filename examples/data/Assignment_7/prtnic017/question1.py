# PRTNIC017
# 28 April 2014
# Receive words and print out unique ones

# List
words = []

# Input
print('Enter strings (end with DONE):')
word = input('')
while word != 'DONE':
    if word not in words:
        words.append(word)
    word = input('')

# Output
print('\nUnique list:')
for w in words:
    print(w)
