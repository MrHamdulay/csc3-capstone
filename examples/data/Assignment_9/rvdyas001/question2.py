"""Yashna Ravidas 
paragraph
15 May 2014"""
import textwrap
filename=input("Enter the input filename:\n")
infile= open(filename, "r")
lines = infile.read()
infile.close()
filenames=input("Enter the output filename:\n")
outfile= open(filenames, "w")

width=eval(input("Enter the line width:\n"))


text = textwrap.dedent(lines).strip()
for length in [width]:
       print (textwrap.fill(text, length=length), outfile)
       
outfile.close()



