"""format text into paragraphs of given field width
blessings hadebe
15 may 2014"""


infile=input("Enter the input filename:\n")
outfile=input("Enter the output filename:\n")
width=eval(input('Enter the line width:\n'))

f=open(infile, "r")
x=f.readlines()
f.close()

#strip of the \n character from the end of each line in the original file, except where a new paragraph exists
strings=""
for line in range(len(x)):
    if line !=len(x):
        if x[line] != '\n':
            strings+=x[line][:-1] + " "
        else:
            strings+=x[line]
    else:
        strings+=x[line]
strings=strings.split("\n") #strings becomes a list with the different paragraphs form the original file as seperate items


paragraph=''
def format(y, paragraph):
    """formats a paragraph to the given width"""
    if len(y) < width:
        paragraph+=y
    elif y[width]==' ':
        paragraph= paragraph + y[: width] + '\n'
        return format(y[width +1:], paragraph)
    else:
        x=y[:width]
        z=x[::-1]
        space=z.find(" ")
        spaceindex=width-space
        newline=y[:spaceindex]
        paragraph=paragraph+newline+'\n'
        return format(y[spaceindex:], paragraph)
    return paragraph


out=open(outfile, "w")
out.close

out=open(outfile, "a")

#append new lines of formatted text to the output file
for y in strings:
    if y != strings[-1]:
        y=y.lstrip()
        y=format(y, paragraph)
        print(y, end='\n\n', file=out)
    else:
        y=y.lstrip()
        y=format(y, paragraph)
        print(y, file=out)        
out.close()
