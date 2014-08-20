'''CSC1015F Assign 9 - Q2
Adam Rosendorff - RSNADA001
11 May 2014'''
file_in = input('Enter the input filename:\n')
file_out = input('Enter the output filename:\n')
line_width = input('Enter the line width:\n')
f = open(file_in, 'r')
words = f.read().split(' ')
f.close() 

#remove breaks from words (but not paragraph breaks)
i = 0
while i < (len(words)):
    #a new paragraph marker
    if words[i] == '\n\n':
        True
    #if two words are 'joined' by a \n\n, they must be separated
    elif '\n\n' in words[i]:
        temp = words[i].split('\n\n')
        words[i] = temp[0]
        words.insert(i+1,'\n\n')
        words.insert(i+2,temp[1])
    #removes new lines characters (words in paragraph treated as if on 1 line)
    elif '\n' in words[i]:
        temp = words[i].split('\n')
        words[i] = temp[0]
        words.insert(i+1,temp[1])
    i += 1 #a while loop as it checks len(words) each time

new_f = open(file_out, 'w')       
line = int(line_width)
while len(words) > 0:
    if words[0] == '\n\n':
        new_f.write(words.pop(0))
        line = int(line_width)
    elif len(words[0]) >= line:
        if line > 1:
            new_f.write(' ')
        new_f.write('\n')
        line = int(line_width)
    if line == int(line_width): #if it's the start of a new line
        word_length = len(words[0])
        new_f.write(words.pop(0))
        line -= word_length
    else:
        line -= len(words[0])+1 #+1 to account for single space between words
        new_f.write(' '+words.pop(0))
new_f.close()
