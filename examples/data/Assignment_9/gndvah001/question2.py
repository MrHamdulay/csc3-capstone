import textwrap

infile = input("Enter the input filename:\n")
outfile = input("Enter the output filename:\n")
length = eval(input("Enter the line width:\n"))

#open, read and close file
fin = open(infile, "r")
fl = fin.read()
fin.close

list = textwrap.wrap(fl, width = length)

fout = open (outfile, "w")
for item in list:
    print (item, file=fout)

fout.close ()