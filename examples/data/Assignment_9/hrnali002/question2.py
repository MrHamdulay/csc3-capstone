"""A program to reformat a text file so that lines are at most a given length
Alison Hoernle
HRNALI002
11 May 2014"""

# get all the details from the user

infile = input("Enter the filename:\n")
outfile = input("Enter the output filename:\n")
width = int(input("Enter the line width:\n"))

# open the file that the text is in and store the text as a string
f = open(infile, "r")
lines = f.readlines()
f.close()

#make a list, and each new item is each new word
wordlist = []
for line in lines:
    line = line.split(' ')
    wordlist.append(line)
    
# take out the newline cahracter in each item (except if the only item in the list is the new line (cause then we want a new paragraph))
for line in wordlist:
    if len(line) > 1:
        word = line[-1]
        if word[-1] == '\n':
            word = word[:-1]
            line[-1] = word

# transfer each item to make a 1D array instead of 2D
words = []
for line in wordlist:
    for word in line:
        words.append(word)

# write to the output file
f_o = open(outfile, "w")

print(words[0], end = '', file = f_o) # print the very first word on the very first line
new_line = words[0] # defining the first word to the newline variable ( going to check the length of this newline)
w = 1

for i in range(len(words)-1):
    if words[w] == '\n': #if that's the string, then it's a new paragraph
        print("\n\n", sep = '', end = '', file = f_o)
        new_line = '' #len(newline) must be zero now
    
    elif len(new_line) + len(' ') + len(words[w]) <= width: # if it's all less than the prescribed width, then add the space and the next word
        if new_line != '':
            new_line =  new_line + ' ' + words[w] #length of the newline adds the space plus the word we've just printed
            print(' ', words[w], sep = '', end = '', file = f_o)
        else:
            new_line = words[w]
            print(words[w], end = '', file = f_o)
    
    else: # if it goes over the prescribed width, then go onto a new line and make the newline variable this new word that we print on the new line.
        print('\n', words[w], sep = '', end = '', file = f_o)
        new_line = words[w]
    w += 1
        
f_o.close()