# Student Number: PRTNIC017
# Date: 5/11/14
# Description:
#       A program to reformat a text file so that all lines are
#       at most a given length.

# Input
infile = open(input('Enter the input filename:\n'), 'r')

outfile = open(input('Enter the output filename:\n'), 'w+')
wid = eval(input('Enter the line width:\n'))

# Read file as paragraphs
paragraphs = []
t = []  # list of words in paragraph
for l in infile.readlines():
    l = l.replace('\n', '')
    if l != '':
        t += l.split(' ')
    elif l == '':
        paragraphs.append(t)
        t = []
# add that last paragraph to the list
paragraphs.append(t)
# close the input file
infile.close()

# Write out paragraphs apart
for pindex in range(len(paragraphs)):
    p = paragraphs[pindex]
    line = ''
    index = 0
    while index < len(p):  # make sure to write every word in the paragraph
        if len(line + ' ' + p[index]) <= wid:
            # prevent unnecessary space at beginning of line while adding the word
            if line != '':
                line += ' ' + p[index]
            else:
                line = p[index]
            # move to next word
            index += 1
        else:
            outfile.write(line + '\n')
            line = ''
    if line.strip() != '':
        outfile.write(line + '\n')
    # Write empty line before new paragraph
    if pindex < len(paragraphs):
        outfile.write('\n')
outfile.close()