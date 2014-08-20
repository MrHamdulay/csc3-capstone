'''question2.py
format a file to a given line length
douglas newton NWTDOU001
15 may 2014'''

# get input filename from user
input_file = input('Enter the input filename:\n')

# get output filename from user
output_file = input('Enter output filename:\n')

# get length of line from user
length = eval(input('Enter the line width:\n'))

file = open(input_file,'r')
lines = file.readlines()
file.close()

words = []
for line in lines:
    # if the newline is a paragraph, insert a number 0 as the element
    if line=='\n':
        words.append(0)
    # otherwise simply add all the words from that line
    for word in line.rstrip().split(' '):
        words.append(word)

# open output file to write to it
file = open(output_file,'w')

# set up a counter and line buffer
counter = 0
line = ''
for i in range(len(words)):
    word = words[i]
    
    # if the word is an int, then there was a newline character
    if type(word) == int:
        # so print line to the file and reset line and counter
        print(line.rstrip(),file=file,sep='')
        print(file=file,sep='')
        counter = 0
        line = ''
        
    # check if the word can fit on line
    # note: counter>0 means a space needs to be added, but at 0 it doesn't
    # because the first word of the line is being added
    elif counter + len(word) + (1 if 0<counter else 0) < length + 1:
        # if counter is more than 0, add a space too before word
        if counter>0:
            line += ' '
            counter += 1
        # add the word to the line
        counter += len(word)
        line += word
    else:
        # print the line to the file and reset line and counter
        print(line.rstrip(),file=file,sep='')
        line = word
        counter = len(word)
# print the remaining line
print(line.rstrip(),file=file,sep='')

# close the file
file.close()