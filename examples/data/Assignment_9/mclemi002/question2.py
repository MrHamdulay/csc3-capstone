"""emile mclennan
11/5/14
q2 A9"""
import textwrap
inFile = input('Enter the input filename:\n')
outFile = input('Enter the output filename:\n')
wid= eval(input('Enter the line width:\n'))

wid=40

f = open(inFile,'r') #read in text file
lines = f.read()
f.close()

paragraph = textwrap.wrap(lines, width=wid) #format paragraph

f = open(outFile, 'w') #write to file
for i in paragraph:
    print(i, file = f)
f.close()
