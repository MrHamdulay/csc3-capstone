##Matthew Cherry
##13/05/14
##Rewrites text so that a specific number of characters are on each line

filename_in = input('Enter the input filename:\n')
filename_out = input('Enter the output filename:\n')
linewidth = int(input('Enter the line width:\n'))

file_in = open(filename_in, 'r')

text = file_in.read()
paragraphs = text.split('\n\n') #split the text by new paragraphs
words = []

for i in paragraphs: #splits each paragraph into words
    i = i.replace('\n', ' ')
    words.append(i.split(' '))

file_in.close()

output = ''

for paragraph in words:
    current_line = ''
    for i in paragraph: 
        if len(current_line + i) <= linewidth: #if there is space for the new word, add it to the current line
            current_line += (i + ' ')
        else: #if there is not enough space, append the line to the output and begin a new line
            current_line = current_line[:-1] #removes the redundant space at the end of each line
            output += (current_line + '\n')
            current_line = (i+' ')
    output += (current_line + '\n')
    output += '\n' #new paragraph
    
file_out = open(filename_out, 'w')

print(output, file = file_out)

file_out.close()
