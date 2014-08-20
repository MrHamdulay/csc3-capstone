import textwrap

filename = input('Enter the input filename:\n')
output = input('Enter the output filename:\n')
width = eval(input('Enter the line width:\n'))

f = open(filename,'rt')
lines = f.read() #read all lines into a single string
lines = lines.split(' ')

# create a list of words without escape character '\n'
words = []
for word in lines:
    if '\n' in word:
        if word[0] == '\n':
            words.append(word[1:])
        elif word[-1] =='\n':
            words.append(word[:-1])
    else: words.append(word)
f.close()

# create file write words to
out = open(output,'wt')
text = ''
for word in words:
    if words[-1] != word:
        text+=word+' '
    else:
        text+=word
        
text = "\n".join(textwrap.wrap(text, width))
out.write(text)
out.close()