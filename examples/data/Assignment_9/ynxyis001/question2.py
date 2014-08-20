#Reformat text to a given line length
#Jennifer Yuan (YNXYIS001)
#13 May 2014

f_input = input("Enter the input filename:\n") #gets name of file with text
output = input("Enter the output filename:\n") #gets name of file to overwrite
width = input("Enter the line width:\n") #gets width of each line 

import textwrap #python module
f = open(f_input, "r") #open textfile with data
string = f.read() #puts all data into one string
f.close() #closes textfile

string = string.split("\n\n") #splits parargraph in single string into a separate string per paragraph

y = open(output, "w") #writes to a file
for i in range(len(string)): 
    lines = textwrap.wrap(string[i],eval(width)) #creates lines of length (width)
    for i in lines:
        print(i, file=y) #prints lines to output file
    print(file=y) #prints a new line after each paragraph (string) into output file
y.close() #closes output file