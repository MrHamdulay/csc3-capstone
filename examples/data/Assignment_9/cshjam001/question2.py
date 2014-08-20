import textwrap
infile = input("Enter the input filename:\n")
outfile = input("Enter the output filename:\n")
wdth = eval(input("Enter the line width:\n"))
file = open(infile, "r") #Opening file to read
f = file.read()
file.close()
newfile = open(outfile, "w")
lst=textwrap.wrap(f,width=wdth)
for i in lst:
    print(i,file=newfile)
newfile.close()