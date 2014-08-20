"""Program to format text from one file and paste it in another
Dumisani J Nyathi
17-05-2014"""


import textwrap#convinient for wrapping text

#get information from user
infile = input("Enter the input filename:\n")
outfile = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

#extract text from file
reader = open(infile,"r")
lines = reader.read()
reader.close()

#add formatted text to new file
writer = open(outfile,"w")
string = textwrap.wrap(lines,width)
for line in string:
    print(line,file=writer)

writer.close()