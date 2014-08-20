'''NWTDOU001
question1.py
25 april 2014'''

# this will hold each string input by the user
lines = []

# get the first string, displaying the prompt
line = input('Enter strings (end with DONE):\n')

# this will store the length of the longest string
longest = 0

# 'DONE' is the terminating string
while line!='DONE':
    # the 'longest string' comparison: if the current line is longer than this
    # number, longest becomes the length of that string
    if len(line)>longest:
        longest = len(line)
    lines.append(line)
    # get the next string
    line = input('')

print('')

# use right-justification to display each string aligned to the right
print ('Right-aligned list:')
for line in lines:
    print(line.rjust(longest))